import ctypes
from time import sleep as sl
from pynput.keyboard import Key, Listener

# Returs the toggle state of the caps lock key
def capslock_on():
    return ctypes.windll.user32.GetKeyState(0x14) & 1

paused = False
callback = None
lastKey = ""
shift_pressed = False
r_shift_pressed = False

# On key press
def on_press(key, injected):
    global shift_pressed
    global r_shift_pressed

    if paused:
        return

    try:
        keyChar = key.char
    except AttributeError:
        if (key == Key.shift):
            shift_pressed = True
        elif (key == Key.shift_r):
            r_shift_pressed = True

#On key release
def on_release(key, injected):
    global paused
    global shift_pressed
    global r_shift_pressed

    if paused:
        return

    try:
        keyChar = key.char
    except AttributeError:
        if (shift_pressed and r_shift_pressed):
            paused = True
            callback()
            sl(4)
            paused = False
            shift_pressed = False
            r_shift_pressed = False

        if (key == Key.shift):
            shift_pressed = False
        elif (key == Key.shift_r):
            r_shift_pressed = False

# Starts the listening and sets the callback
def listen_keybaord(cb):
    global callback
    callback = cb
    listener = Listener(on_press, on_release)
    listener.start()
