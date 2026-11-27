# frozen_string_literal: true
# Shared rules are independently exercised by mutation tests.
require 'date'
module MaintainerSchema
  def self.check(data)
    errors = []
    rows = lambda do |path, records, fields|
      unless records.is_a?(Array)
        errors << "#{path}: expected a list"
        next
      end
      records.each_with_index do |row, i|
        fields.each do |key|
          errors << "#{path}[#{i}]: required #{key}" unless row.is_a?(Hash) && !row[key].to_s.strip.empty?
        end
      end
    end
    %w[outstanding distinguished broadening testoftime].each do |name|
      path = "_data/#{name}.yml"
      entries = data[path]
      fields = name == 'testoftime' ? %w[year title citation doi] : %w[year name desc]
      rows.call(path, entries, fields)
      next unless entries.is_a?(Array)
      entries.each_with_index do |record, i|
        next unless record.is_a?(Hash)
        errors << "#{path}[#{i}]: year must be four digits" unless record['year'].to_s.match?(/\A\d{4}\z/)
        event = record['awarded']
        errors << "#{path}[#{i}]: unknown awarded event code #{event}" if event && !data.fetch('_data/abbreviations.yml', []).any? { |e| e['word'] == event }
      end
      keys = entries.select { |r| r.is_a?(Hash) }.map { |r| [r['year'].to_s, r['name'] || r['title']] }
      errors << "#{path}: duplicate recipient/year" if keys.uniq != keys
    end
    data.each do |path, front|
      next unless front.is_a?(Hash)
      if path.start_with?('content/organization/policies/') && front['layout'] != 'redirected'
        %w[title permalink].each { |key| errors << "#{path}: required #{key}" if front[key].to_s.strip.empty? }
      end
      if path.start_with?('_posts/')
        %w[title date].each { |key| errors << "#{path}: required #{key}" if front[key].to_s.strip.empty? }
        begin
          value = front['date']
          legacy = path == '_posts/2014-03-03-SIGCSE-2015-Award-Winners.md' && value == 'March 3, 2014'
          value.respond_to?(:to_date) ? value.to_date : (legacy ? Date.parse(value) : Date.iso8601(value.to_s[0, 10]))
        rescue ArgumentError
          errors << "#{path}: date must be YYYY-MM-DD"
        end
      end
      if (app = front['application'])
        unless app.is_a?(Hash)
          errors << "#{path}: application must be a mapping"
          next
        end
        rows.call("#{path} application.schedule", app['schedule'], %w[conference grants deadline notification]) if app.key?('schedule')
        Array(app['schedule']).each do |event|
          next unless event.is_a?(Hash)
          %w[deadline notification].each do |key|
            next if event[key] == '—'
            begin
              Date.iso8601(event[key].to_s)
            rescue ArgumentError
              errors << "#{path}: application.schedule #{event['conference']} #{key} must be YYYY-MM-DD or —"
            end
          end
        end
        %w[maximum_award eligibility history].each { |key| errors << "#{path}: application.#{key} required" if app[key].nil? || app[key].to_s.strip.empty? }
        errors << "#{path}: application.eligibility must be a nonempty list" unless app['eligibility'].is_a?(Array) && !app['eligibility'].empty?
        errors << "#{path}: form required" if front['form'].to_s.empty?
      end
      %w[active previous].each do |key|
        next unless path.include?('committees-task-forces/index.md')
        rows.call("#{path} #{key}", front[key], %w[name items])
        Array(front[key]).each do |group|
          next unless group.is_a?(Hash)
          Array(group['items']).each_with_index do |item, i|
            errors << "#{path} #{group['name']} items[#{i}]: required item or markdown" unless item.is_a?(Hash) && !(item['item'] || item['markdown']).to_s.strip.empty?
          end
        end
      end
      if front['minutes']
        rows.call("#{path} minutes", front['minutes'], %w[year folder approved])
        Array(front['minutes']).each do |board|
          next unless board.is_a?(Hash)
          rows.call("#{path} #{board['year']}", board['approved'], %w[description date])
          Array(board['approved']).each do |meeting|
            begin
              Date.iso8601(meeting['date'].to_s)
            rescue ArgumentError
              errors << "#{path}: minutes date must be YYYY-MM-DD"
            end
          end
        end
      end
    end
    data.each do |path, front|
      next unless front.is_a?(Hash)
      rows.call("#{path} reports", front['reports'], %w[title url]) if path.end_with?('/treasurer.html')
      if path.end_with?('/chair.md') && path.include?('/reports/')
        rows.call("#{path} reports", front['reports'], %w[chair reports])
        Array(front['reports']).each { |group| rows.call("#{path} #{group['chair']}", group['reports'], %w[year title url]) }
      end
      rows.call("#{path} business", front['business'], %w[year date city]) if front['business']
    end
    membership = data['_data/membership.yml'] || {}
    %w[date members countries image].each { |key| errors << "_data/membership.yml: required #{key}" if membership[key].to_s.strip.empty? }
    rows.call('_data/membership.yml categories', membership['categories'], %w[name count percent])
    Array(data['_data/conferences.yml']).each do |series|
      schedule = Array(series['schedule'])
      keys = schedule.map { |event| [event['title'], event['start-date'].to_s] }
      errors << "_data/conferences.yml #{series['id']}: duplicate scheduled event" unless keys.uniq == keys
    end
    board = data.dig('_data/board.yml', 'current-board') || {}
    %w[year term members].each { |key| errors << "_data/board.yml current-board: required #{key}" if board[key].nil? || board[key].to_s.strip.empty? }
    Array(board['members']).each do |member|
      %w[name position image affiliation country email].each do |key|
        errors << "_data/board.yml #{member['name']}: required #{key}" if member[key].to_s.strip.empty?
      end
      errors << "_data/board.yml #{member['name']}: invalid email" unless member['email'].to_s.match?(/\A[^\s@]+@[^\s@]+\.[^\s@]+\z/)
      image = member['image'].to_s
      errors << "_data/board.yml #{member['name']}: portrait missing #{image}" unless File.file?("assets/images/board/current/#{image}")
    end
    (data['_data/policies.yml'] || {}).each do |key, catalog|
      rows.call("_data/policies.yml #{key}", catalog['policies'], %w[title url]) if catalog.is_a?(Hash) && catalog['policies']
    end
    errors
  end
end
