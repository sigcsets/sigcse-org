# frozen_string_literal: true
# Classifications are discovery labels, not new content-ownership decisions.
Jekyll::Hooks.register :site, :post_read do |site|
  (site.pages + site.collections.values.flat_map(&:docs)).each do |page|
    url = page.url
    category = case url
               when %r{\A/(events|conferences)/} then 'Conferences'
               when %r{\A/programs/awards/} then 'Awards'
               when %r{\A/policies/} then 'Policies'
               when %r{\A/(about/(board|reports)|governance/)} then 'Governance'
               when %r{\A/(archives|sigcse|history)/} then 'Historical records'
               else 'Organizational content'
               end
    kind = if page.data['content_type'] == 'conference-legacy'
             'Conference legacy'
           elsif url.start_with?('/news/') && page.data['date']
             'News'
           elsif url.include?('/reports/') || url.include?('/board-history/') || category == 'Historical records' || page.data['year']
             'Historical record'
           else
             'Organizational page'
           end
    page.data['search_category'] = category
    page.data['search_kind'] = kind
    year = page.data['year'] || (page.data['date'] && page.data['date'].strftime('%Y'))
    year ||= url[%r{/(\d{4})(?:\.html|/)}, 1]
    page.data['search_year'] = year.to_s if year
  end
end
