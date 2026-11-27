# frozen_string_literal: true
# Advisory only: never removes records or changes publication status.
require 'yaml'
require 'date'
require 'json'
require 'fileutils'
today = ENV['REVIEW_DATE'] ? Date.iso8601(ENV['REVIEW_DATE']) : Date.today
load_yaml = ->(path) { YAML.safe_load_file(path, permitted_classes: [Date, Time], aliases: true) }
findings = []
Array(load_yaml.call('_data/conferences.yml')).each do |series|
  Array(series['schedule']).each do |event|
    start = Date.iso8601(event['start-date'].to_s)
    finish = event['end-date'] ? Date.iso8601(event['end-date'].to_s) : start
    findings << {source: '_data/conferences.yml', record: event['title'], review: 'Past schedule retained; confirm next event with liaison'} if finish < today
    findings << {source: '_data/conferences.yml', record: event['title'], review: 'Published date unconfirmed; do not invent precise dates'} if event['dates'].to_s.match?(/TBD|TBA/i)
    findings << {source: '_data/conferences.yml', record: event['title'], review: 'Official event URL missing'} if event['website'].to_s.empty?
  end
end
path = 'content/organization/programs/travel-grants/index.md'
text = File.read(path)[/\A---\s*\r?\n(.*?)\r?\n---/m, 1]
front = YAML.safe_load(text, permitted_classes: [Date, Time])
Array(front.dig('application', 'schedule')).each do |event|
  next if event['deadline'] == '—'
  findings << {source: path, record: event['conference'], review: 'Published application deadline is past; retain pending approved update'} if Date.iso8601(event['deadline'].to_s) < today
end
FileUtils.mkdir_p('artifacts')
File.write('artifacts/freshness.json', JSON.pretty_generate({as_of: today.to_s, advisory: true, findings: findings}) + "\n")
puts "Editorial freshness: #{findings.length} advisory findings; see artifacts/freshness.json (no content changed)"
