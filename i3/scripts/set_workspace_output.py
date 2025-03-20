import i3ipc
import subprocess

PRIMARY="eDP-1"
SECONDARY="HDMI-1-0"

i3 = i3ipc.Connection()


def move_workspace(workspace, output):
    i3.command(f"workspace {workspace}")
    i3.command(f'move workspace to output {output}')

def is_monitor_connected(monitor_name):
    result = subprocess.run(["xrandr"], capture_output=True, text=True)
    return f"{monitor_name} connected" in result.stdout

def main():
    if is_monitor_connected(SECONDARY):
        move_workspace("4", SECONDARY)
    

if __name__ == '__main__':
    main()
