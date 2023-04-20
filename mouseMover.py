import pyautogui as pag
import random
import time

my_mac_resolution=[2560,1600] 
curr_mouse_pos=pag.position()
afk_count=0

while True:
    if pag.position()==curr_mouse_pos:
        afk_count+=1
    else:
        afk_count=0
        curr_mouse_pos=pag.position()
        # here we going to move the mouse randomly
    if afk_count>10:
        x=random.randint(1,my_mac_resolution[0])
        y=random.randint(1,my_mac_resolution[1])
        pag.moveTo(x,y,0.5)
        curr_mouse_pos=pag.position()
    print(f"AFK counter: {afk_count}")
    time.sleep(2)