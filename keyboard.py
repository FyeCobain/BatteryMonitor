import ctypes
from time import sleep as sl
from pynput.keyboard import Key, Listener

# Returs the toggle state of the caps lock key
def capslock_on():
    return ctypes.windll.user32.GetKeyState(0x14) & 1

paused = False
callback = None
cmd_pressed = False
insert_pressed = False

# On key press
def on_press(key, injected):
    global cmd_pressed
    global insert_pressed

    if paused:
        return

    try:
        keyChar = key.char
    except AttributeError:
        if key == Key.cmd:
            cmd_pressed = True
        elif key == Key.insert:
            insert_pressed = True

#On key release
def on_release(key, injected):
    global paused
    global cmd_pressed
    global insert_pressed

    if paused:
        return

    try:
        keyChar = key.char
    except AttributeError:
        if cmd_pressed and insert_pressed:
            paused = True
            callback()
            sl(4)
            paused = False
            cmd_pressed = False
            insert_pressed = False

        if key == Key.cmd:
            cmd_pressed = False
        elif key == Key.insert:
            insert_pressed = False

# Starts the listening and sets the callback
def listen_keybaord(cb):
    global callback
    callback = cb
    listener = Listener(on_press, on_release)
    listener.start()
