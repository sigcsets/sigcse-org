# frozen_string_literal: true
# Run after every build, including jekyll serve rebuilds. No stale search bundle.
Jekyll::Hooks.register :site, :post_write do |site|
  runner = File.join(site.source, 'node_modules/pagefind/lib/runner/bin.cjs')
  abort 'Search dependency missing. Run pnpm install --frozen-lockfile (see docs/BUILD.md).' unless File.file?(runner)
  ok = system('node', runner, '--site', site.dest, '--output-subdir', 'pagefind')
  abort 'Pagefind indexing failed; this build must not be packaged.' unless ok
end
