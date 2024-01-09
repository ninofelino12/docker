#!/bin/bash

# Open Visual Studio Code
code &

# Wait for a moment to ensure that VSCode has started
sleep 2

# Get the window ID of the VSCode window
window_id=$(wmctrl -l | grep "Visual Studio Code" | awk '{print $1}')

# Check if the window ID is not empty
if [ -n "$window_id" ]; then
    # Get the screen width
    screen_width=$(wmctrl -d | awk '{print $9}')

    # Calculate the new width (half of the screen)
    new_width=$((screen_width / 2))

    # Move and resize the VSCode window to the left half of the screen
    wmctrl -i -r $window_id -e 0,0,0,$new_width,-1
fi

