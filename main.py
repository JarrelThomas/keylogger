import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(Key):
    global keys, count
    print("(0) pressed".format(Key))
    
def write_file():

def on_release(Key):
    if Key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as Listener:
    Listener.join()