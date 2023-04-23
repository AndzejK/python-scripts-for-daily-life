import pyautogui as pag
import random
import time
import keyboard


# Setting up the letters and numbers
abc=[chr(a) for a in range(ord("a"),ord("z")+1)]
number=[num for num in range(0,10)]
key_are_pressed=abc+number
test_keys=['q','w']

my_mac_resolution=[2560,1600] 
# get the position right off the batt once the app has been launched 
curr_mouse_pos=pag.position() # (1 1)
print(f'My position is once I launcged this script: {curr_mouse_pos}')
afk_count=0

while True:
    # if the mouse has been not moved from the moment launching this app then add 1 to the count
    if pag.position()==curr_mouse_pos:
        #1 (1 1)          (1 1)
        #2 (3 3)          (3 3)   
        afk_count+=1
    else:
        # (2 2)
    # if the current position of the mouse has changed then reset the count
        afk_count=0
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
    # do nothing for 2 sec
    time.sleep(2)