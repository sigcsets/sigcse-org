# frozen_string_literal: true
module Sigcse
  module Presentation
    def self.canonical(url)
      url.sub(/index\.html\z/, '')
    end

    def self.decorate(page, site)
      url = page.url
      nav = Array(site.data['navigation'])
      section = nav.select { |s| Array(s['matches']).any? { |prefix| url.start_with?(prefix) } }
                   .max_by { |s| Array(s['matches']).select { |p| url.start_with?(p) }.map(&:length).max }
      section ||= {'id' => 'about', 'name' => 'About SIGCSE', 'link' => '/about/'} if url.start_with?('/about/')
      section ||= {'id' => 'news', 'name' => 'News', 'link' => '/news/'} if url.start_with?('/news/')
      page.data['section'] = section
      rules = site.data.dig('presentation', 'patterns') || []
      pattern = rules.select { |r| url.start_with?(r['prefix']) }.max_by { |r| r['prefix'].length }
      page.data['pattern'] ||= pattern && pattern['pattern'] || 'article'
      feature = site.data.dig('presentation', 'features', url) || {}
      page.data['feature_photo'] = feature['photo']
      page.data['description'] ||= feature['description']
      if page.data.dig('application', 'schedule')
        page.data['application']['has_past_deadlines'] = page.data['application']['schedule'].any? do |event|
          begin
            Date.parse(event['deadline'].to_s) < site.time.to_date
          rescue ArgumentError
            false
          end
        end
      end
      crumbs = [{'name' => 'Home', 'link' => '/'}]
      crumbs << {'name' => section['name'], 'link' => section['link']} if section && canonical(url) != canonical(section['link'])
      if page.data['conference']
        record = site.data['conferences'].find { |c| c['id'] == page.data['conference'] }
        crumbs << {'name' => 'Conference archives', 'link' => '/archives/'}
        crumbs << {'name' => record['abbreviation'], 'link' => record['archive_url']} if canonical(url) != canonical(record['archive_url'])
      else
        Array(site.data.dig('presentation', 'parents')).each do |parent|
          crumbs << {'name' => parent['name'], 'link' => parent['link']} if url.start_with?(parent['prefix']) && canonical(url) != canonical(parent['link'])
        end
      end
      crumbs << {'name' => page.data['title'], 'link' => nil}
      page.data['breadcrumbs'] = crumbs
    end
  end
end

Jekyll::Hooks.register :site, :post_read do |site|
  documents = site.collections.values.flat_map(&:docs)
  (site.pages + documents).each { |page| Sigcse::Presentation.decorate(page, site) }
end
