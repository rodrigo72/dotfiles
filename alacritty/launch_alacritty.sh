#!/bin/bash

SECONDARY_MONITOR="HDMI-1-0"

current_monitor=$(i3-msg -t get_workspaces | jq -r '.[] | select(.focused==true).output')

if [ "$current_monitor" = "$SECONDARY_MONITOR" ]; then
    alacritty --config-file ~/.config/alacritty/secondary.toml
else
    alacritty --config-file ~/.config/alacritty/primary.toml
fi
