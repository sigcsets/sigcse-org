# frozen_string_literal: true
require 'date'

module Sigcse
  module Schedule
    # A missing end date never becomes an invented published fact. Month-only
    # entries are retained through that month; TBD entries stay unconfirmed.
    def self.entry(event, today)
      return event.merge('status' => 'unconfirmed') if event['dates'].to_s.match?(/TBD|to be/i)
      start = Date.iso8601(event.fetch('start-date').to_s)
      month_only = event['dates'].to_s.match?(/\A[A-Za-z]+\s+\d{4}\z/)
      finish = if event['end-date']
                 Date.iso8601(event['end-date'].to_s)
               elsif month_only
                 Date.new(start.year, start.month, -1)
               else
                 start
               end
      event.merge('status' => (finish < today ? 'past' : 'upcoming'),
                  'sort_date' => (month_only ? Date.new(start.year, start.month, 1) : start).iso8601)
    end

    def self.lists(records, today)
      events = records.flat_map do |series|
        Array(series['schedule']).map do |event|
          entry(event, today).merge('series_id' => series['id'], 'series_name' => series['abbreviation'],
                                    'archive_url' => series['archive_url'])
        end
      end
      [events.select { |e| e['status'] == 'upcoming' }.sort_by { |e| e['sort_date'] },
       events.select { |e| e['status'] == 'unconfirmed' }]
    end
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  upcoming, unconfirmed = Sigcse::Schedule.lists(Array(site.data['conferences']), site.time.to_date)
  Array(site.data['conferences']).each do |series|
    Array(series['schedule']).each { |event| event['display_status'] = Sigcse::Schedule.entry(event, site.time.to_date)['status'] }
  end
  site.data['upcoming_conferences'] = upcoming
  site.data['unconfirmed_conferences'] = unconfirmed
end
