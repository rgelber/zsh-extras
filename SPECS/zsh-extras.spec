Name:           zsh-extras
Version:        2
Release:        2
Summary:        This package allows zsh to perform auto suggestions, syntax highlighting, and history substring. 

Group:          SIERRATEK
BuildArch:      x86_64
License:        GPL
Source0:        zsh-extras-2.tar.gz
Requires:       zsh

%description
This package allows zsh to perform auto suggestions, syntax highlighting, and history substring.

%global debug_package %{nil}

%prep
%setup 

%build

%install
install -m 0775 -d %{buildroot}/etc/skel
install -m 0755 -d %{buildroot}/usr/share/zsh
install -m 0644 zshrc /etc/skel/.zshrc
cp -ra zsh/* %{buildroot}/usr/share/zsh
cp -ra zsh-theme-powerlevel10k %{buildroot}/usr/share/zsh-theme-powerlevel10k

%files
/usr/share/zsh-theme-powerlevel10k
/usr/share/zsh/functions
/usr/share/zsh/scripts
/usr/share/zsh/configs
//usr/share/zsh/plugins
/usr/share/zsh/vendor-completions
/usr/share/zsh/redhat-zsh-config
/usr/share/zsh/redhat-zsh-prompt
/usr/share/zsh/p10k-portable.zsh
/usr/share/zsh/p10k.zsh
/usr/share/zsh/zsh-maia-prompt
/usr/share/zsh/README.md

%changelog
* Tue Sep 11 2022 Ryan Gelber  2.0.2
  - Update plugins and added extended zsh auto completions
  - Added fuzzy search for Cntrl + R

* Tue Apr 23 2019 Ryan Gelber  1.0.0
  - Initial rpm release


