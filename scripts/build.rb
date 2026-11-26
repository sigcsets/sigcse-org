# frozen_string_literal: true
# Always build into a clean, repository-local output; never clean arbitrary paths.
require 'fileutils'
require 'rbconfig'
root = File.expand_path('..', __dir__)
Dir.chdir(root)
mode = ARGV.shift || 'live'
abort 'Usage: bundle exec ruby scripts/build.rb [live|staging|serve]' unless %w[live staging serve].include?(mode)
destination = File.join(root, '_site')
FileUtils.rm_rf(destination)
command = mode == 'serve' ? 'serve' : 'build'
config = mode == 'staging' ? '_config_staging.yml' : '_config_live.yml'
exec(RbConfig.ruby, Gem.bin_path('jekyll', 'jekyll'), command,
     '--config', config, '--destination', destination, '--strict_front_matter',
     * (mode == 'serve' ? ['--host', '127.0.0.1'] : []))
