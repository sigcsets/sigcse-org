# frozen_string_literal: true
require 'addressable/uri'
# Preview-only URL adaptation; source content and other configurations stay intact.
# Runs before search_index.rb so the engine indexes the final public HTML.
Jekyll::Hooks.register :site, :post_write do |site|
  next unless site.config['github_pages_preview']
  prefix = site.baseurl
  cname = File.join(site.dest, 'CNAME')
  File.delete(cname) if File.file?(cname)
  adapt = lambda do |name, ref|
    next ref if ref.start_with?('#', 'data:', 'mailto:', 'tel:', 'javascript:')
    if !ref.start_with?('/') && !ref.match?(%r{\Ahttps?://})
      resolved = Addressable::URI.join("https://sigcsets.github.io#{prefix}/#{name}", ref)
      next ref if resolved.path.start_with?(prefix + '/')
    end
    uri = Addressable::URI.join("https://sigcse.org/#{name}", ref)
    next ref unless %w[sigcse.org www.sigcse.org sigcsets.github.io].include?(uri.host)
    path = uri.path
    path = prefix + '/' + path.sub(%r{\A/}, '') unless path == prefix || path.start_with?(prefix + '/')
    uri.scheme = 'https'
    uri.host = 'sigcsets.github.io'
    uri.path = path
    ref.match?(%r{\A(?:https?:)?//}) ? uri.to_s : uri.request_uri + (uri.fragment ? "##{uri.fragment}" : "")
  end
  Dir.glob(File.join(site.dest, '**', '*.html')).each do |path|
    name = path.delete_prefix(site.dest + '/')
    html = File.read(path)
    html = html.gsub(/(\b(?:href|src|poster)\s*=\s*)(["'])(.*?)\2/im) { match = Regexp.last_match; match[1] + match[2] + adapt.call(name, match[3]) + match[2] }
    html = html.gsub(/(url\s*=\s*)([^"'<>\s]+)/i) { match = Regexp.last_match; match[1] + adapt.call(name, match[2]) }
    html = html.gsub(/(location\s*=\s*)(["'])(.*?)\2/i) { match = Regexp.last_match; match[1] + match[2] + adapt.call(name, match[3]) + match[2] }
    html = html.sub(/<head\b[^>]*>/i) { |head| head + '<meta name="robots" content="noindex, nofollow, noarchive">' }
    File.write(path, html)
  end
  File.write(File.join(site.dest, 'robots.txt'), "User-agent: *\nDisallow: /\n")
end
