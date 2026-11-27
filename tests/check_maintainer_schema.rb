# frozen_string_literal: true
require 'yaml'
require 'date'
require_relative '../scripts/maintainer_schema'
data = {}
Dir.glob('{_data,content,_posts}/**/*.{yml,md,html}').each do |path|
  text = File.read(path, encoding: 'bom|utf-8')
  text = text[/\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n/m, 1] unless path.end_with?('.yml')
  data[path] = YAML.safe_load(text, permitted_classes: [Date, Time], aliases: true) if text
end
abort MaintainerSchema.check(data).join("\n") unless MaintainerSchema.check(data).empty?
cases = [
  ['news date', ->(d) { d['_posts/example.md'] = {'title' => 'Example', 'date' => '2027-02-30'} }],
  ['award citation', ->(d) { d['_data/outstanding.yml'][0].delete('desc') }],
  ['duplicate recipient', ->(d) { d['_data/outstanding.yml'] << d['_data/outstanding.yml'][0].dup }],
  ['unknown award event', ->(d) { d['_data/outstanding.yml'][0]['awarded'] = 'INVALID' }],
  ['missing portrait', ->(d) { d['_data/board.yml']['current-board']['members'][0]['image'] = 'missing-image.png' }],
  ['committee name', ->(d) { d['content/organization/programs/committees-task-forces/index.md']['active'][0].delete('name') }],
  ['funding deadline', ->(d) { d['content/organization/programs/travel-grants/index.md']['application']['schedule'][0].delete('deadline') }],
  ['minutes date', ->(d) { d['content/organization/about/reports/board.md']['minutes'][0]['approved'][0]['date'] = '2027-13-01' }],
  ['policy title', ->(d) { d['_data/policies.yml']['board']['policies'][0].delete('title') }],
  ['membership snapshot', ->(d) { d['_data/membership.yml'].delete('date') }],
  ['report URL', ->(d) { d['content/organization/about/reports/treasurer.html']['reports'][0].delete('url') }]
]
cases.each do |name, change|
  copy = Marshal.load(Marshal.dump(data))
  change.call(copy)
  abort "FAIL: #{name} was accepted" if MaintainerSchema.check(copy).empty?
end
puts "PASS: current maintenance data and #{cases.length} editing-error mutations"
markdown = Marshal.load(Marshal.dump(data))
markdown['content/organization/programs/committees-task-forces/index.md']['active'][0]['items'] << {'markdown' => '[Approved charter](reports/example.pdf)'}
abort 'FAIL: plain Markdown committee item rejected' unless MaintainerSchema.check(markdown).empty?
puts 'PASS: new Markdown committee item schema (in-memory example only)'
