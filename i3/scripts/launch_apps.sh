#!/bin/bash

sleep 2.3

firefox &
sleep 2.2

obsidian &
sleep 3.1

i3-msg 'workspace 2'
alacritty -e cmus &
sleep 0.8

i3-msg 'workspace 3'
alacritty &
sleep 0.8

i3-msg 'workspace 1'

