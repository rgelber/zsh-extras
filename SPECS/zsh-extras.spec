Name:           zsh-extras
Version:        1
Release:        1
Summary:        This package allows zsh to perform auto suggestions, syntax highlighting, and history substring. 

Group:          SIERRATEK
BuildArch:      x86_64
License:        GPL
Source0:        zsh-extras-1.tar.gz
Requires:       zsh redhat-lsb-core

%description
This package allows zsh to perform auto suggestions, syntax highlighting, and history substring.

%global debug_package %{nil}

%pre
if [[ -d /usr/share/zsh/plugins ]]; then
  rm -rf /usr/share/zsh/plugins
fi

if [[ ! -d /usr/share/zsh/plugins ]]; then
  mkdir -p /usr/share/zsh/plugins
fi
%prep
%setup 

%build

%install
install -m 0775 -d %{buildroot}/etc/skel
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.circleci
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-completions
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-completions/src
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-history-substring-search
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/cursor
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/line
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/test-data
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/root
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests
install -m 0644 zsh-autosuggestions/.circleci/config.yml %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.circleci/config.yml
install -m 0644 zsh-autosuggestions/.editorconfig %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.editorconfig
install -m 0644 zsh-autosuggestions/.rspec %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.rspec
install -m 0644 zsh-autosuggestions/.rubocop.yml %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.rubocop.yml
install -m 0644 zsh-autosuggestions/.ruby-version %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.ruby-version
install -m 0644 zsh-autosuggestions/CHANGELOG.md %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/CHANGELOG.md
install -m 0644 zsh-autosuggestions/DESCRIPTION %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/DESCRIPTION
install -m 0644 zsh-autosuggestions/Dockerfile %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Dockerfile
install -m 0644 zsh-autosuggestions/Gemfile %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Gemfile
install -m 0644 zsh-autosuggestions/Gemfile.lock %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Gemfile.lock
install -m 0644 zsh-autosuggestions/INSTALL.md %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/INSTALL.md
install -m 0644 zsh-autosuggestions/LICENSE %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/LICENSE
install -m 0644 zsh-autosuggestions/Makefile %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Makefile
install -m 0644 zsh-autosuggestions/README.md %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/README.md
install -m 0644 zsh-autosuggestions/URL %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/URL
install -m 0644 zsh-autosuggestions/VERSION %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/VERSION
install -m 0644 zsh-autosuggestions/ZSH_VERSIONS %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/ZSH_VERSIONS
install -m 0644 zsh-autosuggestions/install_test_zsh.sh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/install_test_zsh.sh
install -m 0644 zsh-autosuggestions/spec/async_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/async_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/auto_cd_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/auto_cd_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/bracketed_paste_magic_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/bracketed_paste_magic_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/client_zpty_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/client_zpty_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/glob_subst_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/glob_subst_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/rebound_bracket_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/rebound_bracket_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/vi_mode_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/vi_mode_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/wrapped_widget_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/wrapped_widget_spec.rb
install -m 0644 zsh-autosuggestions/spec/integrations/zle_input_stack_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/zle_input_stack_spec.rb
install -m 0644 zsh-autosuggestions/spec/kill_ring_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/kill_ring_spec.rb
install -m 0644 zsh-autosuggestions/spec/line_init_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/line_init_spec.rb
install -m 0644 zsh-autosuggestions/spec/multi_line_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/multi_line_spec.rb
install -m 0644 zsh-autosuggestions/spec/options/buffer_max_size_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/buffer_max_size_spec.rb
install -m 0644 zsh-autosuggestions/spec/options/highlight_style_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/highlight_style_spec.rb
install -m 0644 zsh-autosuggestions/spec/options/original_widget_prefix_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/original_widget_prefix_spec.rb
install -m 0644 zsh-autosuggestions/spec/options/strategy_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/strategy_spec.rb
install -m 0644 zsh-autosuggestions/spec/options/use_async_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/use_async_spec.rb
install -m 0644 zsh-autosuggestions/spec/options/widget_lists_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/widget_lists_spec.rb
install -m 0644 zsh-autosuggestions/spec/spec_helper.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/spec_helper.rb
install -m 0644 zsh-autosuggestions/spec/strategies/completion_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/completion_spec.rb
install -m 0644 zsh-autosuggestions/spec/strategies/history_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/history_spec.rb
install -m 0644 zsh-autosuggestions/spec/strategies/match_prev_cmd_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/match_prev_cmd_spec.rb
install -m 0644 zsh-autosuggestions/spec/strategies/special_characters_helper.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/special_characters_helper.rb
install -m 0644 zsh-autosuggestions/spec/terminal_session.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/terminal_session.rb
install -m 0644 zsh-autosuggestions/spec/widgets/disable_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/disable_spec.rb
install -m 0644 zsh-autosuggestions/spec/widgets/enable_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/enable_spec.rb
install -m 0644 zsh-autosuggestions/spec/widgets/fetch_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/fetch_spec.rb
install -m 0644 zsh-autosuggestions/spec/widgets/toggle_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/toggle_spec.rb
install -m 0644 zsh-autosuggestions/src/async.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/async.zsh
install -m 0644 zsh-autosuggestions/src/bind.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/bind.zsh
install -m 0644 zsh-autosuggestions/src/config.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/config.zsh
install -m 0644 zsh-autosuggestions/src/fetch.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/fetch.zsh
install -m 0644 zsh-autosuggestions/src/highlight.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/highlight.zsh
install -m 0644 zsh-autosuggestions/src/start.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/start.zsh
install -m 0644 zsh-autosuggestions/src/strategies/completion.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/completion.zsh
install -m 0644 zsh-autosuggestions/src/strategies/history.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/history.zsh
install -m 0644 zsh-autosuggestions/src/strategies/match_prev_cmd.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/match_prev_cmd.zsh
install -m 0644 zsh-autosuggestions/src/util.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/util.zsh
install -m 0644 zsh-autosuggestions/src/widgets.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/widgets.zsh
install -m 0644 zsh-autosuggestions/zsh-autosuggestions.plugin.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
install -m 0644 zsh-autosuggestions/zsh-autosuggestions.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
install -m 0644 zsh-completions/.editorconfig %{buildroot}/usr/share/zsh/plugins/zsh-completions/.editorconfig
install -m 0644 zsh-completions/CONTRIBUTING.md %{buildroot}/usr/share/zsh/plugins/zsh-completions/CONTRIBUTING.md
install -m 0644 zsh-completions/LICENSE %{buildroot}/usr/share/zsh/plugins/zsh-completions/LICENSE
install -m 0644 zsh-completions/README.md %{buildroot}/usr/share/zsh/plugins/zsh-completions/README.md
install -m 0644 zsh-completions/src/_afew %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_afew
install -m 0644 zsh-completions/src/_android %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_android
install -m 0644 zsh-completions/src/_archlinux-java %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_archlinux-java
install -m 0644 zsh-completions/src/_artisan %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_artisan
install -m 0644 zsh-completions/src/_atach %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_atach
install -m 0644 zsh-completions/src/_bitcoin-cli %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_bitcoin-cli
install -m 0644 zsh-completions/src/_bower %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_bower
install -m 0644 zsh-completions/src/_bundle %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_bundle
install -m 0644 zsh-completions/src/_caffeinate %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_caffeinate
install -m 0644 zsh-completions/src/_cap %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_cap
install -m 0644 zsh-completions/src/_cask %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_cask
install -m 0644 zsh-completions/src/_ccache %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_ccache
install -m 0644 zsh-completions/src/_cf %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_cf
install -m 0644 zsh-completions/src/_cheat %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_cheat
install -m 0644 zsh-completions/src/_choc %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_choc
install -m 0644 zsh-completions/src/_chromium %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_chromium
install -m 0644 zsh-completions/src/_cmake %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_cmake
install -m 0644 zsh-completions/src/_coffee %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_coffee
install -m 0644 zsh-completions/src/_composer %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_composer
install -m 0644 zsh-completions/src/_conan %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_conan
install -m 0644 zsh-completions/src/_concourse %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_concourse
install -m 0644 zsh-completions/src/_console %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_console
install -m 0644 zsh-completions/src/_cppcheck %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_cppcheck
install -m 0644 zsh-completions/src/_dad %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_dad
install -m 0644 zsh-completions/src/_debuild %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_debuild
install -m 0644 zsh-completions/src/_dget %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_dget
install -m 0644 zsh-completions/src/_dhcpcd %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_dhcpcd
install -m 0644 zsh-completions/src/_diana %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_diana
install -m 0644 zsh-completions/src/_docpad %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_docpad
install -m 0644 zsh-completions/src/_drush %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_drush
install -m 0644 zsh-completions/src/_ecdsautil %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_ecdsautil
install -m 0644 zsh-completions/src/_emulator %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_emulator
install -m 0644 zsh-completions/src/_envdir %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_envdir
install -m 0644 zsh-completions/src/_exportfs %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_exportfs
install -m 0644 zsh-completions/src/_fab %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_fab
install -m 0644 zsh-completions/src/_fail2ban-client %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_fail2ban-client
install -m 0644 zsh-completions/src/_ffind %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_ffind
install -m 0644 zsh-completions/src/_fleetctl %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_fleetctl
install -m 0644 zsh-completions/src/_flutter %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_flutter
install -m 0644 zsh-completions/src/_force %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_force
install -m 0644 zsh-completions/src/_fwupdmgr %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_fwupdmgr
install -m 0644 zsh-completions/src/_gas %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_gas
install -m 0644 zsh-completions/src/_ghc %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_ghc
install -m 0644 zsh-completions/src/_gist %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_gist
install -m 0644 zsh-completions/src/_glances %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_glances
install -m 0644 zsh-completions/src/_golang %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_golang
install -m 0644 zsh-completions/src/_google %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_google
install -m 0644 zsh-completions/src/_gtk-launch %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_gtk-launch
install -m 0644 zsh-completions/src/_hledger %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_hledger
install -m 0644 zsh-completions/src/_homestead %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_homestead
install -m 0644 zsh-completions/src/_httpie %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_httpie
install -m 0644 zsh-completions/src/_ibus %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_ibus
install -m 0644 zsh-completions/src/_include-what-you-use %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_include-what-you-use
install -m 0644 zsh-completions/src/_inxi %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_inxi
install -m 0644 zsh-completions/src/_jmeter %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_jmeter
install -m 0644 zsh-completions/src/_jmeter-plugins %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_jmeter-plugins
install -m 0644 zsh-completions/src/_jonas %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_jonas
install -m 0644 zsh-completions/src/_jrnl %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_jrnl
install -m 0644 zsh-completions/src/_kak %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_kak
install -m 0644 zsh-completions/src/_kitchen %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_kitchen
install -m 0644 zsh-completions/src/_knife %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_knife
install -m 0644 zsh-completions/src/_language_codes %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_language_codes
install -m 0644 zsh-completions/src/_lunchy %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_lunchy
install -m 0644 zsh-completions/src/_mc %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_mc
install -m 0644 zsh-completions/src/_middleman %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_middleman
install -m 0644 zsh-completions/src/_mina %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_mina
install -m 0644 zsh-completions/src/_mix %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_mix
install -m 0644 zsh-completions/src/_mussh %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_mussh
install -m 0644 zsh-completions/src/_mvn %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_mvn
install -m 0644 zsh-completions/src/_nano %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_nano
install -m 0644 zsh-completions/src/_nanoc %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_nanoc
install -m 0644 zsh-completions/src/_nftables %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_nftables
install -m 0644 zsh-completions/src/_node %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_node
install -m 0644 zsh-completions/src/_nvm %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_nvm
install -m 0644 zsh-completions/src/_openssl %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_openssl
install -m 0644 zsh-completions/src/_optirun %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_optirun
install -m 0644 zsh-completions/src/_patool %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_patool
install -m 0644 zsh-completions/src/_perf %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_perf
install -m 0644 zsh-completions/src/_periscope %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_periscope
install -m 0644 zsh-completions/src/_pgsql_utils %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_pgsql_utils
install -m 0644 zsh-completions/src/_phing %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_phing
install -m 0644 zsh-completions/src/_pixz %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_pixz
install -m 0644 zsh-completions/src/_pkcon %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_pkcon
install -m 0644 zsh-completions/src/_play %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_play
install -m 0644 zsh-completions/src/_pm2 %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_pm2
install -m 0644 zsh-completions/src/_port %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_port
install -m 0644 zsh-completions/src/_protoc %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_protoc
install -m 0644 zsh-completions/src/_pygmentize %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_pygmentize
install -m 0644 zsh-completions/src/_rails %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_rails
install -m 0644 zsh-completions/src/_ralio %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_ralio
install -m 0644 zsh-completions/src/_redis-cli %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_redis-cli
install -m 0644 zsh-completions/src/_rfkill %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_rfkill
install -m 0644 zsh-completions/src/_rkt %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_rkt
install -m 0644 zsh-completions/src/_rslsync %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_rslsync
install -m 0644 zsh-completions/src/_rspec %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_rspec
install -m 0644 zsh-completions/src/_rsvm %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_rsvm
install -m 0644 zsh-completions/src/_rubocop %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_rubocop
install -m 0644 zsh-completions/src/_sbt %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_sbt
install -m 0644 zsh-completions/src/_scala %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_scala
install -m 0644 zsh-completions/src/_scrub %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_scrub
install -m 0644 zsh-completions/src/_sdd %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_sdd
install -m 0644 zsh-completions/src/_setcap %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_setcap
install -m 0644 zsh-completions/src/_setup.py %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_setup.py
install -m 0644 zsh-completions/src/_sfdx %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_sfdx
install -m 0644 zsh-completions/src/_showoff %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_showoff
install -m 0644 zsh-completions/src/_srm %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_srm
install -m 0644 zsh-completions/src/_stack %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_stack
install -m 0644 zsh-completions/src/_subl %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_subl
install -m 0644 zsh-completions/src/_subliminal %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_subliminal
install -m 0644 zsh-completions/src/_supervisorctl %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_supervisorctl
install -m 0644 zsh-completions/src/_svm %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_svm
install -m 0644 zsh-completions/src/_tarsnap %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_tarsnap
install -m 0644 zsh-completions/src/_teamocil %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_teamocil
install -m 0644 zsh-completions/src/_thor %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_thor
install -m 0644 zsh-completions/src/_tmuxinator %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_tmuxinator
install -m 0644 zsh-completions/src/_tmuxp %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_tmuxp
install -m 0644 zsh-completions/src/_tox %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_tox
install -m 0644 zsh-completions/src/_trash-empty %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_trash-empty
install -m 0644 zsh-completions/src/_trash-list %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_trash-list
install -m 0644 zsh-completions/src/_trash-put %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_trash-put
install -m 0644 zsh-completions/src/_trash-restore %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_trash-restore
install -m 0644 zsh-completions/src/_udisksctl %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_udisksctl
install -m 0644 zsh-completions/src/_ufw %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_ufw
install -m 0644 zsh-completions/src/_vagrant %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_vagrant
install -m 0644 zsh-completions/src/_virtualbox %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_virtualbox
install -m 0644 zsh-completions/src/_vnstat %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_vnstat
install -m 0644 zsh-completions/src/_wemux %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_wemux
install -m 0644 zsh-completions/src/_wg-quick %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_wg-quick
install -m 0644 zsh-completions/src/_xinput %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_xinput
install -m 0644 zsh-completions/src/_xsel %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_xsel
install -m 0644 zsh-completions/src/_yaourt %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_yaourt
install -m 0644 zsh-completions/src/_yarn %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_yarn
install -m 0644 zsh-completions/src/_zcash-cli %{buildroot}/usr/share/zsh/plugins/zsh-completions/src/_zcash-cli
install -m 0644 zsh-completions/zsh-completions-howto.org %{buildroot}/usr/share/zsh/plugins/zsh-completions/zsh-completions-howto.org
install -m 0644 zsh-completions/zsh-completions.plugin.zsh %{buildroot}/usr/share/zsh/plugins/zsh-completions/zsh-completions.plugin.zsh
install -m 0644 zsh-history-substring-search/README.md %{buildroot}/usr/share/zsh/plugins/zsh-history-substring-search/README.md
install -m 0644 zsh-history-substring-search/zsh-history-substring-search.plugin.zsh %{buildroot}/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.plugin.zsh
install -m 0644 zsh-history-substring-search/zsh-history-substring-search.zsh %{buildroot}/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
install -m 0644 zshrc %{buildroot}/usr/share/zsh/plugins/zshrc
install -m 0644 zsh-syntax-highlighting/.editorconfig %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/.editorconfig
install -m 0644 zsh-syntax-highlighting/.revision-hash %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/.revision-hash
install -m 0644 zsh-syntax-highlighting/.travis.yml %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/.travis.yml
install -m 0644 zsh-syntax-highlighting/.version %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/.version
install -m 0644 zsh-syntax-highlighting/COPYING.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/COPYING.md
install -m 0644 zsh-syntax-highlighting/HACKING.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/HACKING.md
install -m 0644 zsh-syntax-highlighting/INSTALL.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/INSTALL.md
install -m 0644 zsh-syntax-highlighting/Makefile %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/Makefile
install -m 0644 zsh-syntax-highlighting/README.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/README.md
install -m 0644 zsh-syntax-highlighting/changelog.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/changelog.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters/brackets.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/brackets.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters/cursor.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/cursor.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters/line.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/line.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters/main.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/main.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters/pattern.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/pattern.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters/regexp.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/regexp.md
install -m 0644 zsh-syntax-highlighting/docs/highlighters/root.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/root.md
install -m 0644 zsh-syntax-highlighting/highlighters/README.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/README.md
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/brackets-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/brackets-highlighter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket-line-finish.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket-line-finish.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/empty-styles.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/empty-styles.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/loop-styles.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/loop-styles.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/mismatch-patentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/mismatch-patentheses.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/near-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/near-quotes.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/nested-parentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/nested-parentheses.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/only-error.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/only-error.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/quoted-patentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/quoted-patentheses.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/simple-parentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/simple-parentheses.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/cursor/cursor-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/cursor/cursor-highlighter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/line/line-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/line/line-highlighter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/main-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/main-highlighter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position1b.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position1b.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position3b.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position3b.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position5.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position5.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-assignment1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-assignment1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-basic.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-basic.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-command-substitution.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-command-substitution.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-comment1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-comment2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-complex.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-complex.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-empty.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-empty.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-eponymous1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-eponymous1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-eponymous2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-eponymous2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-in-cmdsubst.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-in-cmdsubst.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-loop.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-loop.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-loop2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-loop2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-nested-precommand.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested-precommand.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-nested.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-parameter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-parameter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-quoted.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-redirect.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-redirect.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse5.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse5.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-self.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-self.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir1b.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir1b.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-unknown-token1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-unknown-token1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias-unknown-token2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-unknown-token2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/alias.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/always1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/always2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/always3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/anonymous-function.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/anonymous-function.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arg0-colon.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arg0-colon.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arith-cmdsubst-mess.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arith-cmdsubst-mess.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arith1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arith1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arith2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arith2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-command-substitution.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-command-substitution.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-doubled-parens.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-doubled-parens.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-empty.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-empty.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-evaluation.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-evaluation.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-hist-expn.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-hist-expn.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-invalid-chars.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-invalid-chars.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-multiplication.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-multiplication.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-nested.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-nested.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-quoted.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-unclosed.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-unclosed.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-unfinished.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-unfinished.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-append.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-append.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-argv.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-argv.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-array.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-array2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-array3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-invalid-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-invalid-command.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-quoted-cmdsubst.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-quoted-cmdsubst.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-semicolon.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-semicolon.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-subshell.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-subshell.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-value-quote1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-value-quote1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign-value-quote2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-value-quote2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assign.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword5.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword5.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/assignment-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-quoted.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-argument.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-argument.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-open.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-open.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/backslash-space.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-space.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/backslash.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-array.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-array.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-scalar.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-scalar.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/bang-pipeline.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-pipeline.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/braces1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/braces1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/braces2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/braces2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch10-if-negative.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch10-if-negative.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch5.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch5.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch6.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch6.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch7.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch7.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8-if-positive.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8-if-positive.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch9-if-positive.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch9-if-positive.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/cdpath-abspath.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/cdpath-abspath.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-premature-termination.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-premature-termination.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/cmdpos-elision-partial.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/cmdpos-elision-partial.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-adjacent.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-adjacent.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-in-assignment.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-in-assignment.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-unclosed.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-unclosed.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/commandseparator.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/commandseparator.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/comment-followed.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-followed.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/comment-leading.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-leading.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/comment-off.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-off.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/comments.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comments.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/commmand-parameter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/commmand-parameter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/control-flow.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/control-flow2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/control-flow3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/cthulhu.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/cthulhu.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dinbrack1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dinbrack1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dirs_blacklist.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dirs_blacklist.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-dollar.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-dollar.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-noise.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-noise.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-paren.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-paren.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/double-hyphen-option.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-hyphen-option.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/empty-command-newline.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command-newline.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/empty-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/empty-command2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/empty-line.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-line.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/equals1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/equals2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/equals3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/equals4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/escaped-single-quote.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/escaped-single-quote.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/exec-redirection1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/exec-redirection1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/fd-target-not-filename.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/fd-target-not-filename.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/function-altsyntax.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-altsyntax.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/function-named1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/function-named2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/function.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/glob.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/glob.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/global-alias1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/global-alias1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/globs-with-quoting.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/globs-with-quoting.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/hashed-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/hashed-command.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-escaped.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-escaped.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-followed.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-followed.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-no.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-no.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-unescaped.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-unescaped.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-yes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-yes.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/history-expansion.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/history-expansion2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/inheritance.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/inheritance.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/loop-newline.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/loop-newline.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/meta-no-eval1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/meta-no-eval1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/meta-no-eval2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/meta-no-eval2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/multiline-array-assignment1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-array-assignment1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/multiline-string.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/multiline-string2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/multios-negates-globbing.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multios-negates-globbing.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/multios-negates-globbing2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multios-negates-globbing2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/multiple-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-quotes.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/multiple-redirections.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-redirections.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/noglob-alias.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-alias.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/noglob-always.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-always.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/noglob1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/noglob2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/noglob3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/noglob4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/null-exec.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/null-exec.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/number_range-glob.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/number_range-glob.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/off-by-one.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/off-by-one.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/opt-shwordsplit1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/opt-shwordsplit1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/optimized-cmdsubst-input.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/optimized-cmdsubst-input.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/option-dollar-quote-isnt-filename.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-dollar-quote-isnt-filename.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/option-path_dirs.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-path_dirs.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/option-with-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-with-quotes.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/order-path-after-dollar.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-after-dollar.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/order-path-before-globbing.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-before-globbing.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/param-positional-in-array-append.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/param-positional-in-array-append.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/param-precommand-option-argument1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/param-precommand-option-argument1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/param-precommand-option-argument3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/param-precommand-option-argument3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-elision-command-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-elision-command-word.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-expansion-untokenized1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-expansion-untokenized1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-expansion-untokenized2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-expansion-untokenized2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-star.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-star.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-to-global-alias.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-to-global-alias.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-value-contains-command-position1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-value-contains-command-position1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-value-contains-command-position2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-value-contains-command-position2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/pasted-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/pasted-quotes.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-broken-symlink.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-broken-symlink.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3b.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3b.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-mixed-quoting.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-mixed-quoting.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-separators.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-separators2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-space.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-space.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-named.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-named.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/subshell.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/subshell.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path_prefix.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path_prefix2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/path_prefix3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/plain-file-in-command-position.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/plain-file-in-command-position.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-killing1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-killing1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-killing2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-killing2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-then-assignment.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-then-assignment.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-type1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-type2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-type3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-uninstalled.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-uninstalled.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-unknown-option.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-unknown-option.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/precommand4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand4.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/prefix-redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/prefix-redirection.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-after-redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-after-redirection.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-redirection-isnt-globbing.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-redirection-isnt-globbing.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/process-substitution.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/process-substitution2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/quoted-command-substitution-empty.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/quoted-command-substitution-empty.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/quoted-redirection-in-command-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/quoted-redirection-in-command-word.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/rc-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/rc-quotes.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-comment.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-comment.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-from-param.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-from-param.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-in-cmdsubst.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-in-cmdsubst.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-inhibits-elision.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-inhibits-elision.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-is-not-option.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-is-not-option.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-special-cases.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-special-cases.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/redirection3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/reserved-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/reserved-word.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/simple-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-command.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/simple-redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-redirection.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-command.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-comment.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-comment.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-longopt.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-longopt.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection3.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/tilde-command-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/tilde-command-word.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/time-and-nocorrect1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/time-and-nocorrect1.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/time-and-nocorrect2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/time-and-nocorrect2.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/unbackslash.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unbackslash.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/unknown-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unknown-command.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/vanilla-newline.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vanilla-newline.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/main/test-data/vi-linewise-mode.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vi-linewise-mode.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/pattern/pattern-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/pattern-highlighter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/pattern/test-data/rm-rf.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/test-data/rm-rf.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/regexp/regexp-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/regexp-highlighter.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/regexp/test-data/complex.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/complex.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/regexp/test-data/subexpression.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/subexpression.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/regexp/test-data/word-boundary.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/word-boundary.zsh
install -m 0644 zsh-syntax-highlighting/highlighters/root/root-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/root/root-highlighter.zsh
install -m 0644 zsh-syntax-highlighting/images/after1-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1-smaller.png
install -m 0644 zsh-syntax-highlighting/images/after1.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1.png
install -m 0644 zsh-syntax-highlighting/images/after2-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2-smaller.png
install -m 0644 zsh-syntax-highlighting/images/after2.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2.png
install -m 0644 zsh-syntax-highlighting/images/after3-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3-smaller.png
install -m 0644 zsh-syntax-highlighting/images/after3.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3.png
install -m 0644 zsh-syntax-highlighting/images/after4-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after4-smaller.png
install -m 0644 zsh-syntax-highlighting/images/before1-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1-smaller.png
install -m 0644 zsh-syntax-highlighting/images/before1.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1.png
install -m 0644 zsh-syntax-highlighting/images/before2-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2-smaller.png
install -m 0644 zsh-syntax-highlighting/images/before2.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2.png
install -m 0644 zsh-syntax-highlighting/images/before3-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3-smaller.png
install -m 0644 zsh-syntax-highlighting/images/before3.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3.png
install -m 0644 zsh-syntax-highlighting/images/before4-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before4-smaller.png
install -m 0644 zsh-syntax-highlighting/images/preview-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview-smaller.png
install -m 0644 zsh-syntax-highlighting/images/preview.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview.png
install -m 0644 zsh-syntax-highlighting/release.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/release.md
install -m 0644 zsh-syntax-highlighting/tests/README.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/README.md
install -m 0644 zsh-syntax-highlighting/tests/edit-failed-tests %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/edit-failed-tests
install -m 0644 zsh-syntax-highlighting/tests/generate.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/generate.zsh
install -m 0644 zsh-syntax-highlighting/tests/tap-colorizer.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-colorizer.zsh
install -m 0644 zsh-syntax-highlighting/tests/tap-filter %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-filter
install -m 0644 zsh-syntax-highlighting/tests/test-highlighting.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-highlighting.zsh
install -m 0644 zsh-syntax-highlighting/tests/test-perfs.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-perfs.zsh
install -m 0644 zsh-syntax-highlighting/tests/test-zprof.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-zprof.zsh
install -m 0644 zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh
install -m 0644 zsh-syntax-highlighting/zsh-syntax-highlighting.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
install -m 644 zshrc %{buildroot}/etc/skel/.zshrc-extras

# Install Fuzzy Functions
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/bin
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/doc
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/man
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/man/man1
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/plugin
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/shell
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/src
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/src/algo
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/src/protector
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/src/tui
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/src/util
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/fzf/test

install -m 0755 fzf/bin/fzf-tmux %{buildroot}/usr/share/zsh/plugins/fzf/bin/fzf-tmux
install -m 0755 fzf/bin/fzf %{buildroot}/usr/share/zsh/plugins/fzf/bin/fzf
install -m 0644 fzf/BUILD.md %{buildroot}/usr/share/zsh/plugins/fzf/BUILD.md
install -m 0644 fzf/CHANGELOG.md %{buildroot}/usr/share/zsh/plugins/fzf/CHANGELOG.md
install -m 0644 fzf/doc/fzf.txt %{buildroot}/usr/share/zsh/plugins/fzf/doc/fzf.txt
install -m 0644 fzf/Dockerfile %{buildroot}/usr/share/zsh/plugins/fzf/Dockerfile
install -m 0644 fzf/go.mod %{buildroot}/usr/share/zsh/plugins/fzf/go.mod
install -m 0644 fzf/go.sum %{buildroot}/usr/share/zsh/plugins/fzf/go.sum
install -m 0644 fzf/install %{buildroot}/usr/share/zsh/plugins/fzf/install
install -m 0644 fzf/install.ps1 %{buildroot}/usr/share/zsh/plugins/fzf/install.ps1
install -m 0644 fzf/LICENSE %{buildroot}/usr/share/zsh/plugins/fzf/LICENSE
install -m 0644 fzf/main.go %{buildroot}/usr/share/zsh/plugins/fzf/main.go
install -m 0644 fzf/Makefile %{buildroot}/usr/share/zsh/plugins/fzf/Makefile
install -m 0644 fzf/man/man1/fzf-tmux.1 %{buildroot}/usr/share/zsh/plugins/fzf/man/man1/fzf-tmux.1
install -m 0644 fzf/man/man1/fzf.1 %{buildroot}/usr/share/zsh/plugins/fzf/man/man1/fzf.1
install -m 0644 fzf/plugin/fzf.vim %{buildroot}/usr/share/zsh/plugins/fzf/plugin/fzf.vim
install -m 0644 fzf/README.md %{buildroot}/usr/share/zsh/plugins/fzf/README.md
install -m 0644 fzf/README-VIM.md %{buildroot}/usr/share/zsh/plugins/fzf/README-VIM.md
install -m 0644 fzf/shell/completion.bash %{buildroot}/usr/share/zsh/plugins/fzf/shell/completion.bash
install -m 0644 fzf/shell/completion.zsh %{buildroot}/usr/share/zsh/plugins/fzf/shell/completion.zsh
install -m 0644 fzf/shell/key-bindings.bash %{buildroot}/usr/share/zsh/plugins/fzf/shell/key-bindings.bash
install -m 0644 fzf/shell/key-bindings.fish %{buildroot}/usr/share/zsh/plugins/fzf/shell/key-bindings.fish
install -m 0644 fzf/shell/key-bindings.zsh %{buildroot}/usr/share/zsh/plugins/fzf/shell/key-bindings.zsh
install -m 0644 fzf/src/LICENSE %{buildroot}/usr/share/zsh/plugins/fzf/src/LICENSE
install -m 0644 fzf/src/algo/algo.go %{buildroot}/usr/share/zsh/plugins/fzf/src/algo/algo.go
install -m 0644 fzf/src/algo/algo_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/algo/algo_test.go
install -m 0644 fzf/src/algo/normalize.go %{buildroot}/usr/share/zsh/plugins/fzf/src/algo/normalize.go
install -m 0644 fzf/src/ansi.go %{buildroot}/usr/share/zsh/plugins/fzf/src/ansi.go
install -m 0644 fzf/src/ansi_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/ansi_test.go
install -m 0644 fzf/src/cache.go %{buildroot}/usr/share/zsh/plugins/fzf/src/cache.go
install -m 0644 fzf/src/cache_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/cache_test.go
install -m 0644 fzf/src/chunklist.go %{buildroot}/usr/share/zsh/plugins/fzf/src/chunklist.go
install -m 0644 fzf/src/chunklist_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/chunklist_test.go
install -m 0644 fzf/src/constants.go %{buildroot}/usr/share/zsh/plugins/fzf/src/constants.go
install -m 0644 fzf/src/core.go %{buildroot}/usr/share/zsh/plugins/fzf/src/core.go
install -m 0644 fzf/src/history.go %{buildroot}/usr/share/zsh/plugins/fzf/src/history.go
install -m 0644 fzf/src/history_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/history_test.go
install -m 0644 fzf/src/item.go %{buildroot}/usr/share/zsh/plugins/fzf/src/item.go
install -m 0644 fzf/src/item_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/item_test.go
install -m 0644 fzf/src/matcher.go %{buildroot}/usr/share/zsh/plugins/fzf/src/matcher.go
install -m 0644 fzf/src/merger.go %{buildroot}/usr/share/zsh/plugins/fzf/src/merger.go
install -m 0644 fzf/src/merger_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/merger_test.go
install -m 0644 fzf/src/options.go %{buildroot}/usr/share/zsh/plugins/fzf/src/options.go
install -m 0644 fzf/src/options_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/options_test.go
install -m 0644 fzf/src/pattern.go %{buildroot}/usr/share/zsh/plugins/fzf/src/pattern.go
install -m 0644 fzf/src/pattern_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/pattern_test.go
install -m 0644 fzf/src/protector/protector.go %{buildroot}/usr/share/zsh/plugins/fzf/src/protector/protector.go
install -m 0644 fzf/src/protector/protector_openbsd.go %{buildroot}/usr/share/zsh/plugins/fzf/src/protector/protector_openbsd.go
install -m 0644 fzf/src/reader.go %{buildroot}/usr/share/zsh/plugins/fzf/src/reader.go
install -m 0644 fzf/src/reader_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/reader_test.go
install -m 0644 fzf/src/result.go %{buildroot}/usr/share/zsh/plugins/fzf/src/result.go
install -m 0644 fzf/src/result_others.go %{buildroot}/usr/share/zsh/plugins/fzf/src/result_others.go
install -m 0644 fzf/src/result_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/result_test.go
install -m 0644 fzf/src/result_x86.go %{buildroot}/usr/share/zsh/plugins/fzf/src/result_x86.go
install -m 0644 fzf/src/terminal.go %{buildroot}/usr/share/zsh/plugins/fzf/src/terminal.go
install -m 0644 fzf/src/terminal_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/terminal_test.go
install -m 0644 fzf/src/terminal_unix.go %{buildroot}/usr/share/zsh/plugins/fzf/src/terminal_unix.go
install -m 0644 fzf/src/terminal_windows.go %{buildroot}/usr/share/zsh/plugins/fzf/src/terminal_windows.go
install -m 0644 fzf/src/tokenizer.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tokenizer.go
install -m 0644 fzf/src/tokenizer_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tokenizer_test.go
install -m 0644 fzf/src/tui/dummy.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/dummy.go
install -m 0644 fzf/src/tui/light.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/light.go
install -m 0644 fzf/src/tui/light_unix.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/light_unix.go
install -m 0644 fzf/src/tui/light_windows.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/light_windows.go
install -m 0644 fzf/src/tui/tcell.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/tcell.go
install -m 0644 fzf/src/tui/ttyname_unix.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/ttyname_unix.go
install -m 0644 fzf/src/tui/ttyname_windows.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/ttyname_windows.go
install -m 0644 fzf/src/tui/tui.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/tui.go
install -m 0644 fzf/src/tui/tui_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/tui/tui_test.go
install -m 0644 fzf/src/util/atomicbool.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/atomicbool.go
install -m 0644 fzf/src/util/atomicbool_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/atomicbool_test.go
install -m 0644 fzf/src/util/chars.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/chars.go
install -m 0644 fzf/src/util/chars_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/chars_test.go
install -m 0644 fzf/src/util/eventbox.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/eventbox.go
install -m 0644 fzf/src/util/eventbox_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/eventbox_test.go
install -m 0644 fzf/src/util/slab.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/slab.go
install -m 0644 fzf/src/util/util.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/util.go
install -m 0644 fzf/src/util/util_test.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/util_test.go
install -m 0644 fzf/src/util/util_unix.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/util_unix.go
install -m 0644 fzf/src/util/util_windows.go %{buildroot}/usr/share/zsh/plugins/fzf/src/util/util_windows.go
install -m 0644 fzf/test/fzf.vader %{buildroot}/usr/share/zsh/plugins/fzf/test/fzf.vader
install -m 0644 fzf/test/test_go.rb %{buildroot}/usr/share/zsh/plugins/fzf/test/test_go.rb
install -m 0644 fzf/uninstall %{buildroot}/usr/share/zsh/plugins/fzf/uninstall
install -m 0644 fzf/.fzf.zsh %{buildroot}/usr/share/zsh/plugins/fzf/.fzf.zsh
install -m 0644 fzf/.fzf.bash %{buildroot}/usr/share/zsh/plugins/fzf/.fzf.bash

%files
/usr/share/zsh/plugins
/usr/share/zsh/plugins/zsh-autosuggestions
/usr/share/zsh/plugins/zsh-autosuggestions/.circleci
/usr/share/zsh/plugins/zsh-autosuggestions/.circleci/config.yml
/usr/share/zsh/plugins/zsh-autosuggestions/.editorconfig
/usr/share/zsh/plugins/zsh-autosuggestions/.rspec
/usr/share/zsh/plugins/zsh-autosuggestions/.rubocop.yml
/usr/share/zsh/plugins/zsh-autosuggestions/.ruby-version
/usr/share/zsh/plugins/zsh-autosuggestions/CHANGELOG.md
/usr/share/zsh/plugins/zsh-autosuggestions/DESCRIPTION
/usr/share/zsh/plugins/zsh-autosuggestions/Dockerfile
/usr/share/zsh/plugins/zsh-autosuggestions/Gemfile
/usr/share/zsh/plugins/zsh-autosuggestions/Gemfile.lock
/usr/share/zsh/plugins/zsh-autosuggestions/INSTALL.md
/usr/share/zsh/plugins/zsh-autosuggestions/LICENSE
/usr/share/zsh/plugins/zsh-autosuggestions/Makefile
/usr/share/zsh/plugins/zsh-autosuggestions/README.md
/usr/share/zsh/plugins/zsh-autosuggestions/URL
/usr/share/zsh/plugins/zsh-autosuggestions/VERSION
/usr/share/zsh/plugins/zsh-autosuggestions/ZSH_VERSIONS
/usr/share/zsh/plugins/zsh-autosuggestions/install_test_zsh.sh
/usr/share/zsh/plugins/zsh-autosuggestions/spec
/usr/share/zsh/plugins/zsh-autosuggestions/spec/async_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/auto_cd_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/bracketed_paste_magic_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/client_zpty_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/glob_subst_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/rebound_bracket_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/vi_mode_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/wrapped_widget_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/zle_input_stack_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/kill_ring_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/line_init_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/multi_line_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/buffer_max_size_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/highlight_style_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/original_widget_prefix_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/strategy_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/use_async_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/widget_lists_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/spec_helper.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/completion_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/history_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/match_prev_cmd_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/special_characters_helper.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/terminal_session.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/disable_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/enable_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/fetch_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/toggle_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/src
/usr/share/zsh/plugins/zsh-autosuggestions/src/async.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/bind.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/config.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/fetch.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/highlight.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/start.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies
/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/completion.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/history.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/match_prev_cmd.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/util.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/widgets.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
/usr/share/zsh/plugins/zsh-completions
/usr/share/zsh/plugins/zsh-completions/.editorconfig
/usr/share/zsh/plugins/zsh-completions/CONTRIBUTING.md
/usr/share/zsh/plugins/zsh-completions/LICENSE
/usr/share/zsh/plugins/zsh-completions/README.md
/usr/share/zsh/plugins/zsh-completions/src
/usr/share/zsh/plugins/zsh-completions/src/_afew
/usr/share/zsh/plugins/zsh-completions/src/_android
/usr/share/zsh/plugins/zsh-completions/src/_archlinux-java
/usr/share/zsh/plugins/zsh-completions/src/_artisan
/usr/share/zsh/plugins/zsh-completions/src/_atach
/usr/share/zsh/plugins/zsh-completions/src/_bitcoin-cli
/usr/share/zsh/plugins/zsh-completions/src/_bower
/usr/share/zsh/plugins/zsh-completions/src/_bundle
/usr/share/zsh/plugins/zsh-completions/src/_caffeinate
/usr/share/zsh/plugins/zsh-completions/src/_cap
/usr/share/zsh/plugins/zsh-completions/src/_cask
/usr/share/zsh/plugins/zsh-completions/src/_ccache
/usr/share/zsh/plugins/zsh-completions/src/_cf
/usr/share/zsh/plugins/zsh-completions/src/_cheat
/usr/share/zsh/plugins/zsh-completions/src/_choc
/usr/share/zsh/plugins/zsh-completions/src/_chromium
/usr/share/zsh/plugins/zsh-completions/src/_cmake
/usr/share/zsh/plugins/zsh-completions/src/_coffee
/usr/share/zsh/plugins/zsh-completions/src/_composer
/usr/share/zsh/plugins/zsh-completions/src/_conan
/usr/share/zsh/plugins/zsh-completions/src/_concourse
/usr/share/zsh/plugins/zsh-completions/src/_console
/usr/share/zsh/plugins/zsh-completions/src/_cppcheck
/usr/share/zsh/plugins/zsh-completions/src/_dad
/usr/share/zsh/plugins/zsh-completions/src/_debuild
/usr/share/zsh/plugins/zsh-completions/src/_dget
/usr/share/zsh/plugins/zsh-completions/src/_dhcpcd
/usr/share/zsh/plugins/zsh-completions/src/_diana
/usr/share/zsh/plugins/zsh-completions/src/_docpad
/usr/share/zsh/plugins/zsh-completions/src/_drush
/usr/share/zsh/plugins/zsh-completions/src/_ecdsautil
/usr/share/zsh/plugins/zsh-completions/src/_emulator
/usr/share/zsh/plugins/zsh-completions/src/_envdir
/usr/share/zsh/plugins/zsh-completions/src/_exportfs
/usr/share/zsh/plugins/zsh-completions/src/_fab
/usr/share/zsh/plugins/zsh-completions/src/_fail2ban-client
/usr/share/zsh/plugins/zsh-completions/src/_ffind
/usr/share/zsh/plugins/zsh-completions/src/_fleetctl
/usr/share/zsh/plugins/zsh-completions/src/_flutter
/usr/share/zsh/plugins/zsh-completions/src/_force
/usr/share/zsh/plugins/zsh-completions/src/_fwupdmgr
/usr/share/zsh/plugins/zsh-completions/src/_gas
/usr/share/zsh/plugins/zsh-completions/src/_ghc
/usr/share/zsh/plugins/zsh-completions/src/_gist
/usr/share/zsh/plugins/zsh-completions/src/_glances
/usr/share/zsh/plugins/zsh-completions/src/_golang
/usr/share/zsh/plugins/zsh-completions/src/_google
/usr/share/zsh/plugins/zsh-completions/src/_gtk-launch
/usr/share/zsh/plugins/zsh-completions/src/_hledger
/usr/share/zsh/plugins/zsh-completions/src/_homestead
/usr/share/zsh/plugins/zsh-completions/src/_httpie
/usr/share/zsh/plugins/zsh-completions/src/_ibus
/usr/share/zsh/plugins/zsh-completions/src/_include-what-you-use
/usr/share/zsh/plugins/zsh-completions/src/_inxi
/usr/share/zsh/plugins/zsh-completions/src/_jmeter
/usr/share/zsh/plugins/zsh-completions/src/_jmeter-plugins
/usr/share/zsh/plugins/zsh-completions/src/_jonas
/usr/share/zsh/plugins/zsh-completions/src/_jrnl
/usr/share/zsh/plugins/zsh-completions/src/_kak
/usr/share/zsh/plugins/zsh-completions/src/_kitchen
/usr/share/zsh/plugins/zsh-completions/src/_knife
/usr/share/zsh/plugins/zsh-completions/src/_language_codes
/usr/share/zsh/plugins/zsh-completions/src/_lunchy
/usr/share/zsh/plugins/zsh-completions/src/_mc
/usr/share/zsh/plugins/zsh-completions/src/_middleman
/usr/share/zsh/plugins/zsh-completions/src/_mina
/usr/share/zsh/plugins/zsh-completions/src/_mix
/usr/share/zsh/plugins/zsh-completions/src/_mussh
/usr/share/zsh/plugins/zsh-completions/src/_mvn
/usr/share/zsh/plugins/zsh-completions/src/_nano
/usr/share/zsh/plugins/zsh-completions/src/_nanoc
/usr/share/zsh/plugins/zsh-completions/src/_nftables
/usr/share/zsh/plugins/zsh-completions/src/_node
/usr/share/zsh/plugins/zsh-completions/src/_nvm
/usr/share/zsh/plugins/zsh-completions/src/_openssl
/usr/share/zsh/plugins/zsh-completions/src/_optirun
/usr/share/zsh/plugins/zsh-completions/src/_patool
/usr/share/zsh/plugins/zsh-completions/src/_perf
/usr/share/zsh/plugins/zsh-completions/src/_periscope
/usr/share/zsh/plugins/zsh-completions/src/_pgsql_utils
/usr/share/zsh/plugins/zsh-completions/src/_phing
/usr/share/zsh/plugins/zsh-completions/src/_pixz
/usr/share/zsh/plugins/zsh-completions/src/_pkcon
/usr/share/zsh/plugins/zsh-completions/src/_play
/usr/share/zsh/plugins/zsh-completions/src/_pm2
/usr/share/zsh/plugins/zsh-completions/src/_port
/usr/share/zsh/plugins/zsh-completions/src/_protoc
/usr/share/zsh/plugins/zsh-completions/src/_pygmentize
/usr/share/zsh/plugins/zsh-completions/src/_rails
/usr/share/zsh/plugins/zsh-completions/src/_ralio
/usr/share/zsh/plugins/zsh-completions/src/_redis-cli
/usr/share/zsh/plugins/zsh-completions/src/_rfkill
/usr/share/zsh/plugins/zsh-completions/src/_rkt
/usr/share/zsh/plugins/zsh-completions/src/_rslsync
/usr/share/zsh/plugins/zsh-completions/src/_rspec
/usr/share/zsh/plugins/zsh-completions/src/_rsvm
/usr/share/zsh/plugins/zsh-completions/src/_rubocop
/usr/share/zsh/plugins/zsh-completions/src/_sbt
/usr/share/zsh/plugins/zsh-completions/src/_scala
/usr/share/zsh/plugins/zsh-completions/src/_scrub
/usr/share/zsh/plugins/zsh-completions/src/_sdd
/usr/share/zsh/plugins/zsh-completions/src/_setcap
/usr/share/zsh/plugins/zsh-completions/src/_setup.py
/usr/share/zsh/plugins/zsh-completions/src/_sfdx
/usr/share/zsh/plugins/zsh-completions/src/_showoff
/usr/share/zsh/plugins/zsh-completions/src/_srm
/usr/share/zsh/plugins/zsh-completions/src/_stack
/usr/share/zsh/plugins/zsh-completions/src/_subl
/usr/share/zsh/plugins/zsh-completions/src/_subliminal
/usr/share/zsh/plugins/zsh-completions/src/_supervisorctl
/usr/share/zsh/plugins/zsh-completions/src/_svm
/usr/share/zsh/plugins/zsh-completions/src/_tarsnap
/usr/share/zsh/plugins/zsh-completions/src/_teamocil
/usr/share/zsh/plugins/zsh-completions/src/_thor
/usr/share/zsh/plugins/zsh-completions/src/_tmuxinator
/usr/share/zsh/plugins/zsh-completions/src/_tmuxp
/usr/share/zsh/plugins/zsh-completions/src/_tox
/usr/share/zsh/plugins/zsh-completions/src/_trash-empty
/usr/share/zsh/plugins/zsh-completions/src/_trash-list
/usr/share/zsh/plugins/zsh-completions/src/_trash-put
/usr/share/zsh/plugins/zsh-completions/src/_trash-restore
/usr/share/zsh/plugins/zsh-completions/src/_udisksctl
/usr/share/zsh/plugins/zsh-completions/src/_ufw
/usr/share/zsh/plugins/zsh-completions/src/_vagrant
/usr/share/zsh/plugins/zsh-completions/src/_virtualbox
/usr/share/zsh/plugins/zsh-completions/src/_vnstat
/usr/share/zsh/plugins/zsh-completions/src/_wemux
/usr/share/zsh/plugins/zsh-completions/src/_wg-quick
/usr/share/zsh/plugins/zsh-completions/src/_xinput
/usr/share/zsh/plugins/zsh-completions/src/_xsel
/usr/share/zsh/plugins/zsh-completions/src/_yaourt
/usr/share/zsh/plugins/zsh-completions/src/_yarn
/usr/share/zsh/plugins/zsh-completions/src/_zcash-cli
/usr/share/zsh/plugins/zsh-completions/zsh-completions-howto.org
/usr/share/zsh/plugins/zsh-completions/zsh-completions.plugin.zsh
/usr/share/zsh/plugins/zsh-history-substring-search
/usr/share/zsh/plugins/zsh-history-substring-search/README.md
/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.plugin.zsh
/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
/usr/share/zsh/plugins/zshrc
/usr/share/zsh/plugins/zsh-syntax-highlighting
/usr/share/zsh/plugins/zsh-syntax-highlighting/.editorconfig
/usr/share/zsh/plugins/zsh-syntax-highlighting/.revision-hash
/usr/share/zsh/plugins/zsh-syntax-highlighting/.travis.yml
/usr/share/zsh/plugins/zsh-syntax-highlighting/.version
/usr/share/zsh/plugins/zsh-syntax-highlighting/COPYING.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/HACKING.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/INSTALL.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/Makefile
/usr/share/zsh/plugins/zsh-syntax-highlighting/README.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/changelog.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/brackets.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/cursor.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/line.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/main.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/pattern.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/regexp.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/root.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/README.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/brackets-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket-line-finish.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/empty-styles.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/loop-styles.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/mismatch-patentheses.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/near-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/nested-parentheses.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/only-error.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/quoted-patentheses.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/simple-parentheses.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/cursor
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/cursor/cursor-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/line
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/line/line-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/main-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position1b.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position3b.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/abspath-in-command-position5.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-assignment1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-basic.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-command-substitution.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-complex.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-empty.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-eponymous1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-eponymous2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-in-cmdsubst.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-loop.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-loop2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested-precommand.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-parameter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-quoted.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-redirect.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-reuse5.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-self.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir1b.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-unknown-token1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-unknown-token2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/anonymous-function.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arg0-colon.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arith-cmdsubst-mess.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arith1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arith2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-command-substitution.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-doubled-parens.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-empty.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-evaluation.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-hist-expn.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-invalid-chars.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-multiplication.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-nested.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-quoted.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-unclosed.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-unfinished.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/array-cmdsep3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-append.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-argv.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-invalid-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-quoted-cmdsubst.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-semicolon.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-subshell.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-value-quote1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-value-quote2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-before-resword5.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assignment-quoted.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-argument.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-open.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-space.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-array.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-scalar.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-pipeline.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/braces1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/braces2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch10-if-negative.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch5.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch6.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch7.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8-if-positive.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch9-if-positive.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/cdpath-abspath.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-premature-termination.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/cmdpos-elision-partial.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-adjacent.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-in-assignment.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-unclosed.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/commandseparator.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-followed.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-leading.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-off.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comments.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/commmand-parameter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/cthulhu.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dinbrack1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dirs_blacklist.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-dollar.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-noise.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-paren.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-hyphen-option.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command-newline.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-line.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/equals4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/escaped-single-quote.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/exec-redirection1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/fd-target-not-filename.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-altsyntax.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/glob.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/global-alias1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/globs-with-quoting.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/hashed-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-escaped.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-followed.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-no.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-unescaped.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-yes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/inheritance.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/loop-newline.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/meta-no-eval1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/meta-no-eval2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-array-assignment1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multios-negates-globbing.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multios-negates-globbing2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-redirections.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-alias.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-always.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/null-exec.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/number_range-glob.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/off-by-one.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/opt-shwordsplit1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/optimized-cmdsubst-input.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-dollar-quote-isnt-filename.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-path_dirs.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-with-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-after-dollar.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-before-globbing.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/param-positional-in-array-append.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/param-precommand-option-argument1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/param-precommand-option-argument3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-elision-command-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-expansion-untokenized1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-expansion-untokenized2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-star.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-to-global-alias.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-value-contains-command-position1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-value-contains-command-position2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/pasted-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-broken-symlink.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3b.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-mixed-quoting.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-space.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-named.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/subshell.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/plain-file-in-command-position.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-killing1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-killing2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-then-assignment.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-uninstalled.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-unknown-option.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/prefix-redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-after-redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-redirection-isnt-globbing.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/quoted-command-substitution-empty.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/quoted-redirection-in-command-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/rc-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-comment.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-from-param.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-in-cmdsubst.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-inhibits-elision.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-is-not-option.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-special-cases.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/reserved-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-comment.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-longopt.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/tilde-command-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/time-and-nocorrect1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/time-and-nocorrect2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unbackslash.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unknown-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vanilla-newline.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vi-linewise-mode.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/pattern-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/test-data
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/test-data/rm-rf.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/regexp-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/complex.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/subexpression.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/word-boundary.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/root
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/root/root-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/images
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after4-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before4-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/release.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/README.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/edit-failed-tests
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/generate.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-colorizer.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-filter
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-highlighting.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-perfs.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-zprof.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
/etc/skel/.zshrc-extras

# Fuzzy Functions
/usr/share/zsh/plugins/fzf/.fzf.bash
/usr/share/zsh/plugins/fzf/.fzf.zsh
/usr/share/zsh/plugins/fzf/bin/fzf-tmux
/usr/share/zsh/plugins/fzf/bin/fzf
/usr/share/zsh/plugins/fzf/BUILD.md
/usr/share/zsh/plugins/fzf/CHANGELOG.md
/usr/share/zsh/plugins/fzf/doc/fzf.txt
/usr/share/zsh/plugins/fzf/Dockerfile
/usr/share/zsh/plugins/fzf/go.mod
/usr/share/zsh/plugins/fzf/go.sum
/usr/share/zsh/plugins/fzf/install
/usr/share/zsh/plugins/fzf/install.ps1
/usr/share/zsh/plugins/fzf/LICENSE
/usr/share/zsh/plugins/fzf/main.go
/usr/share/zsh/plugins/fzf/Makefile
/usr/share/zsh/plugins/fzf/man/man1/fzf-tmux.1
/usr/share/zsh/plugins/fzf/man/man1/fzf.1
/usr/share/zsh/plugins/fzf/plugin/fzf.vim
/usr/share/zsh/plugins/fzf/README.md
/usr/share/zsh/plugins/fzf/README-VIM.md
/usr/share/zsh/plugins/fzf/shell/completion.bash
/usr/share/zsh/plugins/fzf/shell/completion.zsh
/usr/share/zsh/plugins/fzf/shell/key-bindings.bash
/usr/share/zsh/plugins/fzf/shell/key-bindings.fish
/usr/share/zsh/plugins/fzf/shell/key-bindings.zsh
/usr/share/zsh/plugins/fzf/src/LICENSE
/usr/share/zsh/plugins/fzf/src/algo/algo.go
/usr/share/zsh/plugins/fzf/src/algo/algo_test.go
/usr/share/zsh/plugins/fzf/src/algo/normalize.go
/usr/share/zsh/plugins/fzf/src/ansi.go
/usr/share/zsh/plugins/fzf/src/ansi_test.go
/usr/share/zsh/plugins/fzf/src/cache.go
/usr/share/zsh/plugins/fzf/src/cache_test.go
/usr/share/zsh/plugins/fzf/src/chunklist.go
/usr/share/zsh/plugins/fzf/src/chunklist_test.go
/usr/share/zsh/plugins/fzf/src/constants.go
/usr/share/zsh/plugins/fzf/src/core.go
/usr/share/zsh/plugins/fzf/src/history.go
/usr/share/zsh/plugins/fzf/src/history_test.go
/usr/share/zsh/plugins/fzf/src/item.go
/usr/share/zsh/plugins/fzf/src/item_test.go
/usr/share/zsh/plugins/fzf/src/matcher.go
/usr/share/zsh/plugins/fzf/src/merger.go
/usr/share/zsh/plugins/fzf/src/merger_test.go
/usr/share/zsh/plugins/fzf/src/options.go
/usr/share/zsh/plugins/fzf/src/options_test.go
/usr/share/zsh/plugins/fzf/src/pattern.go
/usr/share/zsh/plugins/fzf/src/pattern_test.go
/usr/share/zsh/plugins/fzf/src/protector/protector.go
/usr/share/zsh/plugins/fzf/src/protector/protector_openbsd.go
/usr/share/zsh/plugins/fzf/src/reader.go
/usr/share/zsh/plugins/fzf/src/reader_test.go
/usr/share/zsh/plugins/fzf/src/result.go
/usr/share/zsh/plugins/fzf/src/result_others.go
/usr/share/zsh/plugins/fzf/src/result_test.go
/usr/share/zsh/plugins/fzf/src/result_x86.go
/usr/share/zsh/plugins/fzf/src/terminal.go
/usr/share/zsh/plugins/fzf/src/terminal_test.go
/usr/share/zsh/plugins/fzf/src/terminal_unix.go
/usr/share/zsh/plugins/fzf/src/terminal_windows.go
/usr/share/zsh/plugins/fzf/src/tokenizer.go
/usr/share/zsh/plugins/fzf/src/tokenizer_test.go
/usr/share/zsh/plugins/fzf/src/tui/dummy.go
/usr/share/zsh/plugins/fzf/src/tui/light.go
/usr/share/zsh/plugins/fzf/src/tui/light_unix.go
/usr/share/zsh/plugins/fzf/src/tui/light_windows.go
/usr/share/zsh/plugins/fzf/src/tui/tcell.go
/usr/share/zsh/plugins/fzf/src/tui/ttyname_unix.go
/usr/share/zsh/plugins/fzf/src/tui/ttyname_windows.go
/usr/share/zsh/plugins/fzf/src/tui/tui.go
/usr/share/zsh/plugins/fzf/src/tui/tui_test.go
/usr/share/zsh/plugins/fzf/src/util/atomicbool.go
/usr/share/zsh/plugins/fzf/src/util/atomicbool_test.go
/usr/share/zsh/plugins/fzf/src/util/chars.go
/usr/share/zsh/plugins/fzf/src/util/chars_test.go
/usr/share/zsh/plugins/fzf/src/util/eventbox.go
/usr/share/zsh/plugins/fzf/src/util/eventbox_test.go
/usr/share/zsh/plugins/fzf/src/util/slab.go
/usr/share/zsh/plugins/fzf/src/util/util.go
/usr/share/zsh/plugins/fzf/src/util/util_test.go
/usr/share/zsh/plugins/fzf/src/util/util_unix.go
/usr/share/zsh/plugins/fzf/src/util/util_windows.go
/usr/share/zsh/plugins/fzf/test/fzf.vader
/usr/share/zsh/plugins/fzf/test/test_go.rb
/usr/share/zsh/plugins/fzf/uninstall
 
%changelog
* Tue Nov 15 2020 Ryan Gelber  1.0.1
  - Update plugins and added extended zsh auto completions
  - Added fuzzy search for Cntrl + R

* Tue Apr 23 2019 Ryan Gelber  1.0.0
  - Initial rpm release


