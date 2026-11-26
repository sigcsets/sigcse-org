# frozen_string_literal: true
require 'jekyll'
require 'yaml'
require_relative '../_plugins/conference_schedule'
require_relative '../_plugins/presentation'

def check(condition, message)
  abort "FAIL: #{message}" unless condition
end

event = {'title' => 'Example', 'start-date' => '2027-02-17', 'end-date' => '2027-02-20', 'dates' => 'Feb 17-20, 2027'}
check(Sigcse::Schedule.entry(event, Date.new(2027, 2, 19))['status'] == 'upcoming', 'in-progress event remains listed')
check(Sigcse::Schedule.entry(event, Date.new(2027, 2, 20))['status'] == 'upcoming', 'inclusive final day')
check(Sigcse::Schedule.entry(event, Date.new(2027, 2, 21))['status'] == 'past', 'concluded event excluded')
month = {'start-date' => '2027-10-23', 'dates' => 'October 2027'}
check(Sigcse::Schedule.entry(month, Date.new(2027, 10, 31))['status'] == 'upcoming', 'month-only date retained through the month')
check(Sigcse::Schedule.entry(month, Date.new(2027, 11, 1))['status'] == 'past', 'month-only entry expires after month')
check(!Sigcse::Schedule.entry(month, Date.new(2027, 10, 1)).key?('end-date'), 'filtering does not invent published end dates')
check(Sigcse::Schedule.entry({'dates' => 'TBD'}, Date.today)['status'] == 'unconfirmed', 'TBD is separate from chronological dates')

root = File.expand_path('..', __dir__)
records = YAML.safe_load_file(File.join(root, '_data/conferences.yml'), permitted_classes: [Date])
upcoming, unconfirmed = Sigcse::Schedule.lists(records.reverse, Date.new(2026, 11, 26))
check(upcoming.map { |e| e['series_id'] } == %w[symposia iticse comped], 'date ordering independent of source order; expired events excluded')
check(unconfirmed.map { |e| e['series_id'] } == ['respect'], 'TBD placeholder is not presented as a confirmed date')
check(records.find { |r| r['id'] == 'icer' }['schedule'].length == 1, 'historical source records preserved')

data = {'navigation' => YAML.safe_load_file(File.join(root, '_data/navigation.yml')),
        'presentation' => YAML.safe_load_file(File.join(root, '_data/presentation.yml')),
        'conferences' => records}
site = Struct.new(:data, :time).new(data, Time.utc(2026, 11, 26))
page_type = Struct.new(:url, :data)
{'/about/board.html' => 'governance', '/about/reports/board.html' => 'governance',
 '/about/bulletin.html' => 'resources', '/programs/travel-grants/' => 'funding',
 '/programs/awards/broadening-nomination.html' => 'awards', '/events/icer/2025.html' => 'conferences'}.each do |url, expected|
  page = page_type.new(url, {'title' => 'Example'})
  Sigcse::Presentation.decorate(page, site)
  check(page.data.dig('section', 'id') == expected, "active section for #{url}")
end
page = page_type.new('/events/iticse/2025.html', {'title' => 'ITiCSE 2025', 'conference' => 'iticse'})
Sigcse::Presentation.decorate(page, site)
check(page.data['breadcrumbs'].map { |c| c['name'] } == ['Home', 'Conferences', 'Conference archives', 'ITiCSE', 'ITiCSE 2025'], 'archive breadcrumb hierarchy')
puts 'PASS: schedule boundaries, preservation, ordering, active sections and breadcrumb hierarchy'
