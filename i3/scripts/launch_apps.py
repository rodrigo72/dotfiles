import i3ipc
import subprocess
import time

PRIMARY = "eDP-1"
SECONDARY = "HDMI-1-0"

i3 = i3ipc.Connection()


def is_monitor_connected(monitor_name):
    result = subprocess.run(["xrandr"], capture_output=True, text=True)
    return f"{monitor_name} connected" in result.stdout

def main():
    time.sleep(2)
    if is_monitor_connected(SECONDARY):
        i3.command("workspace 1; exec firefox")
        time.sleep(2)
        i3.command("workspace 2; exec alacritty")
        time.sleep(1)
        i3.command("workspace 3; exec alacritty -e cmus")
        time.sleep(1)
        i3.command("workspace 4; exec obsidian")
        time.sleep(2)
        i3.command("workspace 1")
    else:
        i3.command("workspace 1; exec alacritty")
        time.sleep(0.7)
        i3.command("workspace 2; exec firefox")
        time.sleep(2)
        i3.command("workspace 3; exec obsidian")
        time.sleep(2.5)
        i3.command("workspace 4; exec alacritty -e cmus")
        time.sleep(1.5)
        i3.command("workspace 2")


if __name__ == '__main__':
    main()
