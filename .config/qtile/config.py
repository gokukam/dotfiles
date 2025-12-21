# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Imports
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder

# Variables
mod = "mod4"
terminal = "alacritty"
browser = "brave"
emacs = "emacsclient -c -a 'emacs'"
clipmenucmd = "clipmenu -i -p 'Select clip'"
wallchangecmd = (
    "find ~/Pictures/Wallpapers -type f | shuf -n 1 | xargs xwallpaper --stretch"
)


# Autostart hook
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call(home)


keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move up/down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod], "h", lazy.layout.shrink(), desc="Shrink window to the left"),
    Key([mod], "l", lazy.layout.grow(), desc="Shrink window to the right"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    # Hotkeys
    Key([mod], "s", lazy.screen.toggle_group(), desc="Switch to last used group"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod, "shift"],
        "w",
        lazy.spawn(wallchangecmd, shell=True),
        desc="Change to random wallpaper",
    ),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.spawn("logout_menu"), desc="Logout menu"),
    # Launching applications
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn apps using rofi"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Spawn terminal"),
    Key([mod, "mod1"], "b", lazy.spawn(browser), desc="Spawn web browser"),
    Key([mod, "mod1"], "f", lazy.spawn("pcmanfm"), desc="Spawn file manager"),
    Key(
        [mod, "mod1"], "p", lazy.spawn(f"{terminal} -T btop -e btop"), desc="Spawn btop"
    ),
    # Media keys
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot"),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("change_volume -ud 1"),
        desc="Volume down",
    ),
    Key(
        [], "XF86AudioRaiseVolume", lazy.spawn("change_volume -ui 1"), desc="Volume up"
    ),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc="Mute/Unmute audio"),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Toggle play/pause",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next audio"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous audio"),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("change_brightness s +1%"),
        desc="Brightness up",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("change_brightness s 1%-"),
        desc="Brightness down",
    ),
    # Launching custom prompts
    KeyChord(
        [mod],
        "p",
        [
            Key([], "c", lazy.spawn(clipmenucmd), desc="Clipboard menu"),
            Key([], "l", lazy.spawn("library_menu"), desc="Library menu"),
            Key([], "p", lazy.spawn("pass_menu -i -p 'Pass'"), desc="Password menu"),
        ],
        desc="Launch a custom menu",
    ),
    # Dunst-related
    KeyChord(
        [mod],
        "d",
        [
            Key([], "c", lazy.spawn("dunstctl close-all"), desc="Clear all"),
            Key([], "space", lazy.spawn("dunstctl close"), desc="Clear topmost"),
            Key([], "h", lazy.spawn("dunstctl history-pop"), desc="Show history"),
            Key([], "t", lazy.spawn("dunstctl set-paused toggle"), desc="Toggle DND"),
        ],
        desc="Perform a Dunst-related action",
    ),
    # Emacs-related
    KeyChord(
        [mod],
        "e",
        [
            Key([], "e", lazy.spawn(emacs), desc="Launch Emacs"),
            Key(
                [],
                "b",
                lazy.spawn(f"{emacs} --eval '(ibuffer)'"),
                desc="Launch Ibuffer",
            ),
            Key(
                [],
                "d",
                lazy.spawn(f"{emacs} --eval '(dired nil)'"),
                desc="Launch Dired",
            ),
            Key(
                [],
                "n",
                lazy.spawn(f"{emacs} --eval '(elfeed)'"),
                desc="Launch Elfeed",
            ),
            Key(
                [],
                "s",
                lazy.spawn(f"{emacs} --eval '(eshell)'"),
                desc="Launch Eshell",
            ),
        ],
        desc="Launch a specific Emacs window",
    ),
]

groups = [
    Group("WWW", layout="monadtall", matches=[Match(wm_class="Brave-browser")]),
    Group("DEV", layout="monadtall"),
    Group("TERM", layout="monadtall"),
    Group(
        "SYS",
        layout="monadtall",
        matches=[Match(wm_class="VirtualBox Manager"), Match(wm_class="Virt-manager")],
    ),
    Group("DOC", layout="monadtall", matches=[Match(wm_class="Zathura")]),
    Group("GFX", layout="floating", matches=[Match(wm_class="Gimp")]),
    Group("VID", layout="monadtall", matches=[Match(wm_class="mpv")]),
]

# Binding Super+i to switch between groups, Super+shift+i to shift window to group
dgroups_key_binder = simple_key_binder(mod)

# Dict of theme colors
colors = {
    "black": "#272822",
    "red": "#f92672",
    "green": "#a6e22e",
    "yellow": "#f4bf75",
    "blue": "#66d9ef",
    "magenta": "#ae81ff",
    "cyan": "#a1efe4",
    "white": "#f8f8f2",
    "grey": "#75715e",
}

layout_theme = {
    "border_width": 2,
    "margin": 5,
    "border_focus": colors["cyan"],
    "border_normal": colors["black"],
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Iosevka Nerd Font",
    fontsize=12,
    padding=3,
    foreground=colors["white"],
    background=colors["black"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=8),
                widget.Image(filename="~/.config/qtile/arch-logo.svg"),
                widget.Sep(padding=8, foreground=colors["grey"]),
                widget.GroupBox(
                    highlight_method="block",
                    font="Ubuntu Bold",
                    fontsize=10,
                    active=colors["cyan"],
                    inactive=colors["grey"],
                    this_current_screen_border=colors["magenta"],
                    block_highlight_text_color=colors["black"],
                    margin_x=5,
                ),
                widget.Sep(padding=10, foreground=colors["grey"]),
                widget.CurrentLayout(foreground=colors["cyan"]),
                widget.Sep(padding=10, foreground=colors["grey"]),
                widget.WindowName(foreground=colors["green"]),
                widget.CPU(
                    fmt="  {}",
                    format="{load_percent}%",
                    foreground=colors["cyan"],
                ),
                widget.Spacer(length=8),
                widget.Memory(
                    fmt=" {}",
                    format="{MemUsed: .0f}{mm}",
                    foreground=colors["yellow"],
                ),
                widget.Spacer(length=8),
                widget.CheckUpdates(
                    fmt="  {}",
                    distro="Arch_checkupdates",
                    update_interval=3600,
                    colour_have_updates=colors["magenta"],
                    execute=f"{terminal} -e sudo pacman -Syu",
                ),
                widget.Spacer(length=8),
                widget.Battery(
                    fmt="󰁹 {}",
                    format="{percent:2.0%} {char}",
                    update_interval=1,
                    foreground=colors["green"],
                    charge_char="󱐋",
                    discharge_char="",
                    notify_below=25,
                ),
                widget.Spacer(length=8),
                widget.Clock(
                    fmt="  {}",
                    format="%a, %b %d - %H:%M",
                    foreground=colors["blue"],
                ),
                widget.Sep(padding=10, foreground=colors["grey"]),
                widget.DoNotDisturb(
                    foreground=colors["red"],
                    fontsize=15,
                    disabled_icon=" ",
                    enabled_icon=" ",
                    padding=0,
                ),
                widget.Systray(icon_size=18),
                widget.Spacer(length=8),
            ],
            24,
            margin=[5, 2, 2, 2],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="confirm"),  # gitk
        Match(wm_class="about"),  # gitk
        Match(wm_class="file_progress"),  # gitk
        Match(wm_class="dialog"),  # gitk
        Match(wm_class="download"),  # gitk
        Match(wm_class="error"),  # gitk
        Match(wm_class="notification"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="splash"),  # gitk
        Match(wm_class="toolbar"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="yad"),  # yad
        Match(wm_class="Gimp"),  # gimp window
        Match(wm_class="Qalculate-gtk"),  # qalculate window
        Match(title="branchdialog"),  # gitk
        Match(title="Save File"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Oracle VM VirtualBox Manager"),  # gitk
        Match(title="btop"),  # terminal window for btop
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
