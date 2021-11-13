#!/opt/homebrew/bin/python3

import pynput.mouse
from pynput import keyboard
from pynput.keyboard import Key
from pynput.mouse import Button
from ctypes import windll
kController = pynput.keyboard.Controller()
mController = pynput.mouse.Controller()


import time
import pyautogui
import pydirectinput
pydirectinput.FAILSAFE = False
global doCheat
doCheat = False

def on_click(x, y, button, pressed):
    #print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    #print("yo 2")
    #return True
    global doCheat
    #if pressed == False:
    #    print("not pressed")
    #print(doCheat)
    #if (not pressed):
    #    pydirectinput.press('space')
        #kController.press(Key.space)
        # kController.release(Key.space)
    if (not pressed) and doCheat:
        doCheat = False 
        time.sleep(.25)
        print("cheat")
        pydirectinput.press('tab')
        pydirectinput.click(982, 978) 
        pydirectinput.press('tab')

        #time.sleep(1)
        #m0Controller.position = (782, 778)
        #mController.press(Button.left)
        #mController.release(Button.left)
        #time.sleep(1)  
        #kController.press(Key.tab)



def on_scroll(x, y, dx, dy):
    #print('Scrolled {0}'.format((x, y)))
    global doCheat
    doCheat = False
    print("on_scroll")
    print(doCheat)

def on_press(key):
    try:
        if key.char == "3":
            # do something
            global doCheat
            doCheat = True
            print("on_press 3")
        else:
            pass
            #print(key.char)
    except AttributeError as ex:
        pass  

def on_release(key):
    try:
        if key.char == "0":
            # Stop listener
            return False
    except AttributeError as ex:    
        pass

def wait_for_user_input():
    kblistener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouselistener = pynput.mouse.Listener(on_click=on_click, on_scroll=on_scroll) 
    mouselistener.start()
    kblistener.start()
    kblistener.join() # wait till listener will stop
    mouselistener.stop()


wait_for_user_input()