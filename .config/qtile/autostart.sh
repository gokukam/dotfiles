#!/usr/bin/env bash
# Script to autostart programs on qtile startup

xset r rate 240 50 &
find ~/Pictures/Wallpapers -type f | shuf -n 1 | xargs xwallpaper --stretch &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom --daemon &
nm-applet &
blueman-applet &
flameshot &
# emacs --daemon &
emacs --init-directory=~/.config/emacs --daemon &
