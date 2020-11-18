# zsh-extras
This is a project to add zsh-autosuggestions, zsh-history-substring-search zsh-syntax-highlighting and fuzzy search functionality. This package build is a x86_64 RPM build that has been tested on CentOS 6, 7, and 8. The idea was to take all of my favorite zsh plugins from github and build a manageable way to deploy it at a global and local level.

Install zsh-extras:
 - sudo yum install https://github.com/rgelber/zsh-extras/raw/master/RPMS/noarch/zsh-extras-1-1.x86_64.rpm

To enable the zsh configuration for a single user:
 - sudo cp -vf /etc/skel/.zshrc-extras /home/$(whoami)/

To enable the zsh configuration globally: 
 - sudo cp -vf /etc/skel/.zshrc-extras /etc/zshrc 
 
To restore the global configuration: 
 - sudo cp -vf /etc/skel/.zshrc /etc/zshrc
 
 Project References:
 - https://github.com/zsh-users/zsh-autosuggestions
 - https://github.com/zsh-users/zsh-history-substring-search
 - https://github.com/zsh-users/zsh-syntax-highlighting
 
