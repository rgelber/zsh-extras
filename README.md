# zsh-extras
This is a project to add zsh-autosuggestions, zsh-history-substring-search and zsh-syntax-highlighting. This package build is a noarch RPM build for any RPM based system. The idea was to take all of my favorite zsh plugins from github and build a manageable way to deploy them on my servers.

To enable the zsh configuration for a single user:
 - sudo cp -vf /etc/skel/.zsh-extras /home/youruser/

To enable the zsh configuration globally: 
 - sudo mv -v /etc/zshrc /etc/zshrc.bak && sudo cp -v /etc/skel/.zsh-extras /etc/zshrc 
 
 Project Refences:
 - https://github.com/zsh-users/zsh-autosuggestions
 - https://github.com/zsh-users/zsh-history-substring-search
 - https://github.com/zsh-users/zsh-syntax-highlighting
 
