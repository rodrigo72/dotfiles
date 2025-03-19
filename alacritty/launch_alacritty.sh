#!/bin/bash

# Set your secondary monitor identifier (find it with xrandr or i3-msg -t get_outputs)
SECONDARY_MONITOR="HDMI-1-0"

# Get current focused monitor
current_monitor=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).output')

# Launch Alacritty with appropriate config
if [ "$current_monitor" = "$SECONDARY_MONITOR" ]; then
    alacritty --config-file ~/.config/alacritty/secondary.toml
else
    alacritty --config-file ~/.config/alacritty/primary.toml
fi
