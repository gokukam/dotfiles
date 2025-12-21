export HISTCONTROL=ignoredups:erasedups           # no duplicate entries
export HISTFILE="$XDG_CACHE_HOME"/bash_history

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
[[ $- == *i* ]] && source /usr/share/blesh/ble.sh --noattach

### SHOPT
shopt -s autocd # change to named directory
shopt -s cdspell # autocorrects cd misspellings
shopt -s cmdhist # save multi-line commands in history as single line
shopt -s dotglob
shopt -s histappend # do not overwrite history
shopt -s expand_aliases # expand aliases
shopt -s extglob

# Ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

# Start fastfetch
fastfetch
source "$XDG_CONFIG_HOME"/bash/aliasrc

# Auto complete commands prefixed with sudo like normal commands
complete -cf sudo

# Enable the Starship prompt
eval "$(starship init bash)"

# Initialize PyEnv
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# ble.sh
[[ ${BLE_VERSION-} ]] && ble-attach
