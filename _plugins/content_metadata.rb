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

# Normalize visual heading levels inside shared-shell pages, preserving text and IDs.
# Historical standalone publications and redirect pages are not touched.
Jekyll::Hooks.register [:pages, :documents], :post_render do |page|
  next unless page.output&.include?('id="main-content"')
  page.output = page.output.sub(/(<main\b[^>]*>)(.*?)(<\/main>)/m) do
    opening, body, closing = Regexp.last_match.captures
    stack = []
    body = body.gsub(/<h([1-6])\b([^>]*)>(.*?)<\/h\1>/m) do
      original, attrs, text = Regexp.last_match.captures
      level = original.to_i
      stack.pop while stack.any? && stack.last[0] >= level
      adjusted = level == 1 ? 1 : (stack.empty? ? 2 : [stack.last[1] + 1, 6].min)
      stack << [level, adjusted]
      "<h#{adjusted}#{attrs}>#{text}</h#{adjusted}>"
    end
    opening + body + closing
  end
end
