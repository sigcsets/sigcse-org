# frozen_string_literal: true
require 'yaml'
require 'date'
require 'csv'
require 'json'
require 'pathname'

ROOT = File.expand_path('..', __dir__)
Dir.chdir(ROOT)
errors = []
data = {}
# Use Git's publication inputs: ignored local drafts/backups are never inspected.
paths = IO.popen(%w[git ls-files -z], &:read).split("\0")
paths += Dir.glob('{_config*,_data/**/*}.{yml,yaml}')
paths.uniq.each do |path|
  next unless File.file?(path)
  next if path.start_with?('audit/', 'docs/')
  text = nil
  begin
    if path.end_with?('.yml', '.yaml')
      text = File.read(path, encoding: 'bom|utf-8')
    elsif path.end_with?('.md', '.html') && !path.start_with?('_includes/', '_layouts/')
      raw = File.read(path, encoding: 'bom|utf-8')
      text = raw[/\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n/m, 1]
      errors << "#{path}: unclosed front matter" if raw.start_with?("---\n", "---\r\n") && !text
    elsif path.end_with?('.csv')
      CSV.read(path, headers: true, encoding: 'bom|utf-8')
    end
    next unless text
    tree = Psych.parse_stream(text, filename: path)
    walk = lambda do |node|
      if node.is_a?(Psych::Nodes::Mapping)
        keys = node.children.each_slice(2).map { |key, _value| key.value }
        keys.tally.each { |key, count| errors << "#{path}: duplicate YAML key #{key}" if count > 1 }
      end
      node.children&.each { |child| walk.call(child) }
    end
    walk.call(tree)
    value = YAML.safe_load(text, permitted_classes: [Date, Time], aliases: true, filename: path)
    data[path] = value
    errors << "#{path}: front matter must be a mapping" if path.end_with?('.md', '.html') && !value.is_a?(Hash)
  rescue StandardError => e
    errors << "#{path}: #{e.message}"
  end
end

def required_rows(errors, rows, fields, path)
  unless rows.is_a?(Array)
    errors << "#{path}: expected a list"
    return
  end
  rows.each_with_index do |row, i|
    fields.each do |field|
      errors << "#{path}[#{i}]: required #{field}" unless row.is_a?(Hash) && row[field] && !row[field].to_s.empty?
    end
  end
end

required_rows(errors, data['_data/navigation.yml'], %w[name link], '_data/navigation.yml')
required_rows(errors, data['_data/events.yml'], %w[name], '_data/events.yml')
required_rows(errors, data['_data/conferences.yml'], %w[id name abbreviation description archive_url schedule], '_data/conferences.yml')
ids = Array(data['_data/conferences.yml']).map { |row| row['id'] }
errors << '_data/conferences.yml: duplicate id' unless ids.uniq.length == ids.length
required_rows(errors, data.dig('_data/board.yml', 'current-board', 'members'),
              %w[name position image], '_data/board.yml current-board members')
%w[symposia iticse icer comped respect virtual].each do |series|
  path = "_data/#{series}.yml"
  record = data[path]
  unless record.is_a?(Hash)
    errors << "#{path}: expected a mapping"
    next
  end
  required_rows(errors, record['conferences'], %w[year], "#{path} conferences")
  years = Array(record['conferences']).filter_map { |r| r['year'] if r.is_a?(Hash) }
  errors << "#{path}: duplicate conference years" unless years.map(&:to_s).uniq.length == years.length
  Array(record['next-conference']).each do |event|
    next unless event.is_a?(Hash) && event['start-date']
    begin
      Date.iso8601(event['start-date'].to_s)
    rescue ArgumentError
      errors << "#{path}: start-date must be YYYY-MM-DD"
    end
  end
end
# Configs remain independently safe for pre-existing build commands.
base = YAML.safe_load_file('_config.yml')
%w[_config_live.yml _config_staging.yml].each do |path|
  config = YAML.safe_load_file(path)
  base.each do |key, value|
    next if key == 'baseurl'
    errors << "#{path}: shared setting #{key} differs from _config.yml" unless config[key] == value
  end
end
known = JSON.parse(File.read('docs/baselines/known-source-issues.json'))
normalized = errors.uniq.map { |error| error.sub(/\Acontent\/organization\//, '') }
regressions = normalized - known
unless regressions.empty?
  warn regressions.join("\n")
  exit 1
end
puts "Existing source issues: #{(normalized & known).length}; resolved: #{(known - normalized).length}"
puts 'Source validation passed: YAML/front matter/CSV syntax, duplicate keys, initial data fields and config parity'
