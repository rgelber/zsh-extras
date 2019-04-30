Name:           zsh-extras
Version:        1
Release:        0
Summary:        This package allows zsh to perform auto suggestions, syntax highlighting, and history substring. 

Group:          SIERRATEK
BuildArch:      noarch
License:        GPL
Source0:        zsh-extras-1.tar.gz
Requires:       zsh redhat-lsb-core

%description
This package allows zsh to perform auto suggestions, syntax highlighting, and history substring.

%pre
mkdir /usr/share/zsh/plugins/

%prep
%setup 

%build

%install
install -m 0775 -d %{buildroot}/etc/skel
install -m 0755 -d %{buildroot}/usr/share/zsh/plugins/zsh-history-substring-search
install -m 0644 zsh-history-substring-search/zsh-history-substring-search.plugin.zsh %{buildroot}/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.plugin.zsh
install -m 0644 zsh-history-substring-search/zsh-history-substring-search.zsh %{buildroot}/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/cursor
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/line
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/test-data
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/root
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images
install -m 755 -d %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests
install -m 644 zsh-syntax-highlighting/.revision-hash %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/.revision-hash
install -m 644 zsh-syntax-highlighting/.travis.yml %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/.travis.yml
install -m 644 zsh-syntax-highlighting/.version %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/.version
install -m 644 zsh-syntax-highlighting/COPYING.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/COPYING.md
install -m 644 zsh-syntax-highlighting/HACKING.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/HACKING.md
install -m 644 zsh-syntax-highlighting/INSTALL.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/INSTALL.md
install -m 644 zsh-syntax-highlighting/Makefile %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/Makefile
install -m 644 zsh-syntax-highlighting/README.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/README.md
install -m 644 zsh-syntax-highlighting/changelog.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/changelog.md
install -m 644 zsh-syntax-highlighting/docs/highlighters.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters.md
install -m 644 zsh-syntax-highlighting/docs/highlighters/brackets.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/brackets.md
install -m 644 zsh-syntax-highlighting/docs/highlighters/cursor.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/cursor.md
install -m 644 zsh-syntax-highlighting/docs/highlighters/line.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/line.md
install -m 644 zsh-syntax-highlighting/docs/highlighters/main.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/main.md
install -m 644 zsh-syntax-highlighting/docs/highlighters/pattern.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/pattern.md
install -m 644 zsh-syntax-highlighting/docs/highlighters/regexp.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/regexp.md
install -m 644 zsh-syntax-highlighting/docs/highlighters/root.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/root.md
install -m 644 zsh-syntax-highlighting/highlighters/README.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/README.md
install -m 644 zsh-syntax-highlighting/highlighters/brackets/brackets-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/brackets-highlighter.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket-line-finish.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket-line-finish.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/cursor-matchingbracket.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/empty-styles.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/empty-styles.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/loop-styles.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/loop-styles.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/mismatch-patentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/mismatch-patentheses.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/near-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/near-quotes.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/nested-parentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/nested-parentheses.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/only-error.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/only-error.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/quoted-patentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/quoted-patentheses.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/simple-parentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/simple-parentheses.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses.zsh
install -m 644 zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/test-data/unclosed-patentheses2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/cursor/cursor-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/cursor/cursor-highlighter.zsh
install -m 644 zsh-syntax-highlighting/highlighters/line/line-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/line/line-highlighter.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/main-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/main-highlighter.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-assignment1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-assignment1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-comment1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-comment2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-complex.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-complex.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-empty.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-empty.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-loop.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-loop.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-nested-precommand.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested-precommand.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-nested.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-quoted.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-redirect.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-redirect.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-self.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-self.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/alias.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/always1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/always2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/always3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/anonymous-function.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/anonymous-function.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/arg0-colon.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arg0-colon.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-evaluation.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-evaluation.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-append.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-append.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-argv.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-argv.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-array.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-array2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-array3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-semicolon.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-semicolon.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign-subshell.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-subshell.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/assign.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-argument.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-argument.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-open.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-open.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/backslash-space.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-space.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-array.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-array.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-scalar.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-assign-scalar.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/bang-pipeline.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/bang-pipeline.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/braces1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/braces1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/braces2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/braces2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-matching2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch10-if-negative.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch10-if-negative.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch4.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch5.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch5.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch6.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch6.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch7.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch7.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8-if-positive.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8-if-positive.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch8.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch9-if-positive.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-mismatch9-if-positive.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/brackets-premature-termination.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-premature-termination.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-in-assignment.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-in-assignment.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-unclosed.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/command-substitution-unclosed.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/commandseparator.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/commandseparator.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/comment-followed.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-followed.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/comment-leading.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-leading.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/comment-off.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comment-off.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/comments.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/comments.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/commmand-parameter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/commmand-parameter.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/control-flow.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/control-flow2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/control-flow3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/control-flow3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/cthulhu.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/cthulhu.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/dirs_blacklist.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dirs_blacklist.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-dollar.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-dollar.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-noise.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-noise.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-paren.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-paren.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/dollar-quoted3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/double-hyphen-option.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-hyphen-option.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/double-quoted4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/double-quoted4.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/empty-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/empty-command2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/empty-line.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-line.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/escaped-single-quote.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/escaped-single-quote.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/exec-redirection1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/exec-redirection1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/function-altsyntax.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-altsyntax.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/function-named1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/function-named2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/function.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/glob.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/glob.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/globs-with-quoting.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/globs-with-quoting.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/hashed-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/hashed-command.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-escaped.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-escaped.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-no.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-no.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-unescaped.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-unescaped.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-yes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-yes.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/history-expansion.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/history-expansion2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/inheritance.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/inheritance.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/loop-newline.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/loop-newline.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/multiline-array-assignment1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-array-assignment1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/multiline-string.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/multiline-string2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/multiple-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-quotes.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/multiple-redirections.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-redirections.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/noglob-alias.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-alias.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/noglob-always.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-always.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/noglob1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/noglob2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/noglob3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/noglob4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob4.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/number_range-glob.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/number_range-glob.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/off-by-one.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/off-by-one.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/option-path_dirs.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-path_dirs.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/option-with-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-with-quotes.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/order-path-after-dollar.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-after-dollar.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/order-path-before-globbing.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-before-globbing.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/parameter-star.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-star.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-broken-symlink.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-broken-symlink.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word4.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-separators.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-separators2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-space.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-space.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-named.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-named.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path_prefix.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path_prefix2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/path_prefix3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-type1.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type1.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-type2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-type3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand-unknown-option.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-unknown-option.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/precommand4.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand4.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/prefix-redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/prefix-redirection.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-redirection-isnt-globbing.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-redirection-isnt-globbing.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/process-substitution.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/process-substitution2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/quoted-command-substitution-empty.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/quoted-command-substitution-empty.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/rc-quotes.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/rc-quotes.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-comment.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-comment.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/redirection-in-cmdsubst.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-in-cmdsubst.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/redirection2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/redirection3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/reserved-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/reserved-word.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/simple-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-command.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/simple-redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-redirection.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/subshell.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/subshell.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-command.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-comment.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-comment.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection2.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection2.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection3.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection3.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/tilde-command-word.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/tilde-command-word.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/unbackslash.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unbackslash.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/unknown-command.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unknown-command.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/vanilla-newline.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vanilla-newline.zsh
install -m 644 zsh-syntax-highlighting/highlighters/main/test-data/vi-linewise-mode.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vi-linewise-mode.zsh
install -m 644 zsh-syntax-highlighting/highlighters/pattern/pattern-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/pattern-highlighter.zsh
install -m 644 zsh-syntax-highlighting/highlighters/pattern/test-data/rm-rf.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/test-data/rm-rf.zsh
install -m 644 zsh-syntax-highlighting/highlighters/regexp/regexp-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/regexp-highlighter.zsh
install -m 644 zsh-syntax-highlighting/highlighters/regexp/test-data/complex.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/complex.zsh
install -m 644 zsh-syntax-highlighting/highlighters/regexp/test-data/subexpression.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/subexpression.zsh
install -m 644 zsh-syntax-highlighting/highlighters/regexp/test-data/word-boundary.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/word-boundary.zsh
install -m 644 zsh-syntax-highlighting/highlighters/root/root-highlighter.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/root/root-highlighter.zsh
install -m 644 zsh-syntax-highlighting/images/after1-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1-smaller.png
install -m 644 zsh-syntax-highlighting/images/after1.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1.png
install -m 644 zsh-syntax-highlighting/images/after2-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2-smaller.png
install -m 644 zsh-syntax-highlighting/images/after2.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2.png
install -m 644 zsh-syntax-highlighting/images/after3-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3-smaller.png
install -m 644 zsh-syntax-highlighting/images/after3.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3.png
install -m 644 zsh-syntax-highlighting/images/before1-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1-smaller.png
install -m 644 zsh-syntax-highlighting/images/before1.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1.png
install -m 644 zsh-syntax-highlighting/images/before2-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2-smaller.png
install -m 644 zsh-syntax-highlighting/images/before2.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2.png
install -m 644 zsh-syntax-highlighting/images/before3-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3-smaller.png
install -m 644 zsh-syntax-highlighting/images/before3.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3.png
install -m 644 zsh-syntax-highlighting/images/preview-smaller.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview-smaller.png
install -m 644 zsh-syntax-highlighting/images/preview.png %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview.png
install -m 644 zsh-syntax-highlighting/release.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/release.md
install -m 644 zsh-syntax-highlighting/tests/README.md %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/README.md
install -m 644 zsh-syntax-highlighting/tests/generate.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/generate.zsh
install -m 644 zsh-syntax-highlighting/tests/tap-colorizer.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-colorizer.zsh
install -m 644 zsh-syntax-highlighting/tests/tap-filter %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-filter
install -m 644 zsh-syntax-highlighting/tests/test-highlighting.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-highlighting.zsh
install -m 644 zsh-syntax-highlighting/tests/test-perfs.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-perfs.zsh
install -m 644 zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh
install -m 644 zsh-syntax-highlighting/zsh-syntax-highlighting.zsh %{buildroot}/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.circleci
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src
install -m 775 -d %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies
install -m 644 zsh-autosuggestions/.circleci/config.yml %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.circleci/config.yml
install -m 644 zsh-autosuggestions/.editorconfig %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.editorconfig
install -m 644 zsh-autosuggestions/.rspec %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.rspec
install -m 644 zsh-autosuggestions/.rubocop.yml %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.rubocop.yml
install -m 644 zsh-autosuggestions/.ruby-version %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/.ruby-version
install -m 644 zsh-autosuggestions/CHANGELOG.md %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/CHANGELOG.md
install -m 644 zsh-autosuggestions/DESCRIPTION %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/DESCRIPTION
install -m 644 zsh-autosuggestions/Dockerfile %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Dockerfile
install -m 644 zsh-autosuggestions/Gemfile %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Gemfile
install -m 644 zsh-autosuggestions/Gemfile.lock %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Gemfile.lock
install -m 644 zsh-autosuggestions/INSTALL.md %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/INSTALL.md
install -m 644 zsh-autosuggestions/LICENSE %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/LICENSE
install -m 644 zsh-autosuggestions/Makefile %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/Makefile
install -m 644 zsh-autosuggestions/README.md %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/README.md
install -m 644 zsh-autosuggestions/URL %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/URL
install -m 644 zsh-autosuggestions/VERSION %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/VERSION
install -m 644 zsh-autosuggestions/ZSH_VERSIONS %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/ZSH_VERSIONS
install -m 644 zsh-autosuggestions/install_test_zsh.sh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/install_test_zsh.sh
install -m 644 zsh-autosuggestions/spec/async_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/async_spec.rb
install -m 644 zsh-autosuggestions/spec/integrations/auto_cd_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/auto_cd_spec.rb
install -m 644 zsh-autosuggestions/spec/integrations/bracketed_paste_magic_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/bracketed_paste_magic_spec.rb
install -m 644 zsh-autosuggestions/spec/integrations/glob_subst_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/glob_subst_spec.rb
install -m 644 zsh-autosuggestions/spec/integrations/rebound_bracket_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/rebound_bracket_spec.rb
install -m 644 zsh-autosuggestions/spec/integrations/vi_mode_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/vi_mode_spec.rb
install -m 644 zsh-autosuggestions/spec/integrations/wrapped_widget_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/wrapped_widget_spec.rb
install -m 644 zsh-autosuggestions/spec/integrations/zle_input_stack_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/zle_input_stack_spec.rb
install -m 644 zsh-autosuggestions/spec/kill_ring_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/kill_ring_spec.rb
install -m 644 zsh-autosuggestions/spec/multi_line_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/multi_line_spec.rb
install -m 644 zsh-autosuggestions/spec/options/buffer_max_size_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/buffer_max_size_spec.rb
install -m 644 zsh-autosuggestions/spec/options/highlight_style_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/highlight_style_spec.rb
install -m 644 zsh-autosuggestions/spec/options/original_widget_prefix_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/original_widget_prefix_spec.rb
install -m 644 zsh-autosuggestions/spec/options/strategy_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/strategy_spec.rb
install -m 644 zsh-autosuggestions/spec/options/use_async_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/use_async_spec.rb
install -m 644 zsh-autosuggestions/spec/options/widget_lists_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/widget_lists_spec.rb
install -m 644 zsh-autosuggestions/spec/spec_helper.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/spec_helper.rb
install -m 644 zsh-autosuggestions/spec/strategies/history_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/history_spec.rb
install -m 644 zsh-autosuggestions/spec/strategies/match_prev_cmd_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/match_prev_cmd_spec.rb
install -m 644 zsh-autosuggestions/spec/strategies/special_characters_helper.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/special_characters_helper.rb
install -m 644 zsh-autosuggestions/spec/terminal_session.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/terminal_session.rb
install -m 644 zsh-autosuggestions/spec/widgets/disable_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/disable_spec.rb
install -m 644 zsh-autosuggestions/spec/widgets/enable_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/enable_spec.rb
install -m 644 zsh-autosuggestions/spec/widgets/fetch_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/fetch_spec.rb
install -m 644 zsh-autosuggestions/spec/widgets/toggle_spec.rb %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/toggle_spec.rb
install -m 644 zsh-autosuggestions/src/async.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/async.zsh
install -m 644 zsh-autosuggestions/src/bind.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/bind.zsh
install -m 644 zsh-autosuggestions/src/config.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/config.zsh
install -m 644 zsh-autosuggestions/src/fetch.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/fetch.zsh
install -m 644 zsh-autosuggestions/src/highlight.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/highlight.zsh
install -m 644 zsh-autosuggestions/src/setup.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/setup.zsh
install -m 644 zsh-autosuggestions/src/start.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/start.zsh
install -m 644 zsh-autosuggestions/src/strategies/history.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/history.zsh
install -m 644 zsh-autosuggestions/src/strategies/match_prev_cmd.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/match_prev_cmd.zsh
install -m 644 zsh-autosuggestions/src/util.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/util.zsh
install -m 644 zsh-autosuggestions/src/widgets.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/src/widgets.zsh
install -m 644 zsh-autosuggestions/zsh-autosuggestions.plugin.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
install -m 644 zsh-autosuggestions/zsh-autosuggestions.zsh %{buildroot}/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
install -m 644 zshrc %{buildroot}/etc/skel/.zshrc-extras

%files
/usr/share/zsh/plugins/zsh-history-substring-search/
/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.plugin.zsh
/usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/.revision-hash
/usr/share/zsh/plugins/zsh-syntax-highlighting/.travis.yml
/usr/share/zsh/plugins/zsh-syntax-highlighting/.version
/usr/share/zsh/plugins/zsh-syntax-highlighting/COPYING.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/HACKING.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/INSTALL.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/Makefile
/usr/share/zsh/plugins/zsh-syntax-highlighting/README.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/changelog.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/brackets.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/cursor.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/line.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/main.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/pattern.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/regexp.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/docs/highlighters/root.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/README.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/brackets/brackets-highlighter.zsh
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
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/cursor/cursor-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/line/line-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/main-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-assignment1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-comment2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-complex.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-empty.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-loop.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested-precommand.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-nested.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-precommand-option-argument2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-quoted.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-redirect.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-self.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias-to-dir.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/alias.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/always3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/anonymous-function.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arg0-colon.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/arithmetic-evaluation.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-append.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-argv.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-array3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-not-array2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-semicolon.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign-subshell.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/assign.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-argument.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/back-quoted-open.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-continuation.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/backslash-space.zsh
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
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/brackets-premature-termination.zsh
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
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-command2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/empty-line.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/escaped-single-quote.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/exec-redirection1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-altsyntax.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function-named2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/function.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/glob.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/globs-with-quoting.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/hashed-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-escaped.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-no.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-unescaped.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-double-quoted-yes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/history-expansion2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/inheritance.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/jobsubst-isnt-glob2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/loop-newline.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-array-assignment1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiline-string2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/multiple-redirections.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-alias.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob-always.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/noglob4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/number_range-glob.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/off-by-one.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-path_dirs.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/option-with-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-after-dollar.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/order-path-before-globbing.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/parameter-star.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-broken-symlink.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-dollared-word4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-separators2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-space.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-home3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path-tilde-named.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/path_prefix3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type1.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-type3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand-unknown-option.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/precommand4.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/prefix-redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution-redirection-isnt-globbing.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/process-substitution2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/quoted-command-substitution-empty.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/rc-quotes.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-comment.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection-in-cmdsubst.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/redirection3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/reserved-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/simple-redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/subshell.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-comment.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection2.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/sudo-redirection3.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/tilde-command-word.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unbackslash.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/unknown-command.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vanilla-newline.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/main/test-data/vi-linewise-mode.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/pattern-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/pattern/test-data/rm-rf.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/regexp-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/complex.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/subexpression.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/regexp/test-data/word-boundary.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/highlighters/root/root-highlighter.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after1.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after2.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/after3.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before1.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before2.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/before3.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview-smaller.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/images/preview.png
/usr/share/zsh/plugins/zsh-syntax-highlighting/release.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/README.md
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/generate.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-colorizer.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/tap-filter
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-highlighting.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/tests/test-perfs.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh
/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
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
/usr/share/zsh/plugins/zsh-autosuggestions/spec/async_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/auto_cd_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/bracketed_paste_magic_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/glob_subst_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/rebound_bracket_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/vi_mode_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/wrapped_widget_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/integrations/zle_input_stack_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/kill_ring_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/multi_line_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/buffer_max_size_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/highlight_style_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/original_widget_prefix_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/strategy_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/use_async_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/options/widget_lists_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/spec_helper.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/history_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/match_prev_cmd_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/strategies/special_characters_helper.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/terminal_session.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/disable_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/enable_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/fetch_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/spec/widgets/toggle_spec.rb
/usr/share/zsh/plugins/zsh-autosuggestions/src/async.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/bind.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/config.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/fetch.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/highlight.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/setup.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/start.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/history.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/strategies/match_prev_cmd.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/util.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/src/widgets.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh
/usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
/etc/skel/.zshrc-extras

%postun 
rm -rf /usr/share/zsh/plugins

%changelog
* Tue Apr 23 2019 Ryan Gelber  1.0.0
  - Initial rpm release
