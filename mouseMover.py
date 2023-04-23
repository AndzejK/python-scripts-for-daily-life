import pyautogui as pag
import random
import time
from pynput import keyboard
import threading

keys_pressed=[]

my_mac_resolution=[2560,1600] 
# get the position right off the batt once the app has been launched 
curr_mouse_pos=pag.position() # (1 1)
afk_count=0

def catch_key(key):
    try:
        key_value=key.char
        print(f'{key} - was pressed')
        keys_pressed.append(key_value)
    except AttributeError:
        key_value=key
        print(f'{key} - was pressed')
        keys_pressed.append(key_value)

def listening_for_key():
    with keyboard.Listener(on_press=catch_key) as listener:
        listener.join()

# Running concurrently listening_for_key() method
listener_thread = threading.Thread(target=listening_for_key)
listener_thread.start()

while True:
    # if the mouse has been not moved from the moment launching this app then add 1 to the count
    if pag.position()==curr_mouse_pos and len(keys_pressed)==0:
        #1 (1 1)          (1 1)
        #2 (3 3)          (3 3)   
        afk_count+=1
    else:
        # (2 2)
    # if the current position of the mouse has changed then reset the count
        afk_count=0
        keys_pressed.clear()
        # get a new position of the mouse 
        curr_mouse_pos=pag.position() # (2 2)
        # once the the count has reached 10 then move the mouse
    if afk_count>11:
        x=random.randint(1,my_mac_resolution[0])
        y=random.randint(1,my_mac_resolution[1])
        pag.moveTo(x,y,0.5) # generated position (3 3)
        # get a new position of the mouse that was not moved by human
        curr_mouse_pos=pag.position() #(3 3)
    #print the count 
    print(f"AFK counter: {afk_count}")
    # count till 2
    time.sleep(2)