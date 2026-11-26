# frozen_string_literal: true
# Compatibility is generated in memory; schedules have one editable source.
Jekyll::Hooks.register :site, :post_read do |site|
  Array(site.data['conferences']).each do |record|
    site.data[record['id']]['next-conference'] = record['schedule']
  end
  site.pages.each do |page|
    next if page.data['title'] && !page.data['title'].empty?
    series = page.data['conference']
    year = File.basename(page.path, File.extname(page.path))
    record = series && Array(site.data.dig(series, 'conferences')).find { |item| item['year'].to_s == year }
    page.data['title'] = record && record['title'] || year.tr('-_', ' ').split.map(&:capitalize).join(' ')
  end
end
