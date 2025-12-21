# Basic Vars
export TERM="xterm-256color"
export TERMINAL="alacritty"
export BROWSER="brave"
export EDITOR="nvim"
export VISUAL="emacsclient -c -a 'emacs'"
export CM_LAUNCHER="rofi"

# Set manpager
export MANPAGER="sh -c 'col -bx | bat -l man -p'"
export MANROFFOPT='-c'

# XDG
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_SCREENSHOTS_DIR="$HOME/Pictures/Screenshots"

# GTK
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc

# Make apps use XDG_BASE_DIR
export LESSHISTFILE="-"
export INPUTRC="${XDG_CONFIG_HOME:-$HOME/.config}/bash/inputrc"
export PASSWORD_STORE_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/password-store"
export GOPATH="${XDG_DATA_HOME:-$HOME/.local/share}/go"

# Fix apps
export QT_QPA_PLATFORMTHEME="qt5ct"
export MOZ_USE_XINPUT2="1" # Mozilla smooth scrolling/touchpads.
export AWT_TOOLKIT="MToolkit wmname LG3D"
export _JAVA_AWT_WM_NONREPARENTING=1
export GNUPGHOME="$XDG_DATA_HOME"/gnupg
export GPG_TTY=$(tty)
export _ble_contrib_fzf_base=/usr/bin/fzf

# Python
export PYENV_ROOT="$HOME/.pyenv"

# PATH
if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$GOPATH/bin" ] ;
  then PATH="$GOPATH/bin:$PATH"
fi

if [ -d "$PYENV_ROOT" ] ;
  then PATH="$PYENV_ROOT/bin:$PATH"
fi

# Source bashrc
[[ -f ~/.bashrc ]] && . ~/.bashrc
