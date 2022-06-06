from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
 
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
#Store Size: (region=(472,922,1011,158))
#Store 1: (region=(480,928,192,143))
#Store 2: (region=(681,928,192,143))
#Store 3: (region=(882,928,192,143))
#Store 4: (region=(1084,928,192,143))
#Store 5: (region=(1285,928,192,143))

while keyboard.is_pressed('m') == False:
    #Store 2
        pic = pyautogui.screenshot(region=(472,922,1011,158))
        width, height = pic.size #This saves the width & height of the variable "pic"
        if pyautogui.locateOnScreen('Ziggs.png', confidence=0.95) != None:
            click(570,990)
            print("Ziggs Store 1")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Poppy.png', confidence=0.95) != None:
            click(570,990)
            print("Poppy Store 1")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Lulu.png', confidence=0.95) != None:
            click(570,990)
            print("Lulu Store 1")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Corki.png', confidence=0.95) != None:
            click(570,990)
            print("Corki Store 1")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Gnar.png', confidence=0.95) != None:
            click(570,990)
            print("Gnar Store 1")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Vex.png', confidence=0.95) != None:
            click(570,990)
            print("Vex Store 1")
            time.sleep(0.01)
            
    #Store 2
        pic = pyautogui.screenshot(region=(472,922,1011,158))
        width, height = pic.size #This saves the width & height of the variable "pic"
        if pyautogui.locateOnScreen('Ziggs.png', confidence=0.95) != None:
            click(770,990)
            print("Ziggs Store 2")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Poppy.png', confidence=0.95) != None:
            click(770,990)
            print("Poppy Store 2")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Lulu.png', confidence=0.95) != None:
            click(770,990)
            print("Lulu Store 2")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Corki.png', confidence=0.95) != None:
            click(770,990)
            print("Corki Store 2")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Gnar.png', confidence=0.95) != None:
            click(770,990)
            print("Gnar Store 2")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Vex.png', confidence=0.95) != None:
            click(770,990)
            print("Vex Store 2")
            time.sleep(0.01)
        
    
    #Store 3
        pic = pyautogui.screenshot(region=(472,922,1011,158))
        width, height = pic.size #This saves the width & height of the variable "pic"
        if pyautogui.locateOnScreen('Ziggs.png', confidence=0.95) != None:
            click(970,990)
            print("Ziggs Store 3")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Poppy.png', confidence=0.95) != None:
            click(970,990)
            print("Poppy Store 3")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Lulu.png', confidence=0.95) != None:
            click(970,990)
            print("Lulu Store 3")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Corki.png', confidence=0.95) != None:
            click(970,990)
            print("Corki Store 3")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Gnar.png', confidence=0.95) != None:
            click(970,990)
            print("Gnar Store 3")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Vex.png', confidence=0.95) != None:
            click(970,990)
            print("Vex Store 3")
            time.sleep(0.01)
        

    #Store 4
        pic = pyautogui.screenshot(region=(472,922,1011,158))
        width, height = pic.size #This saves the width & height of the variable "pic"
        if pyautogui.locateOnScreen('Ziggs.png', confidence=0.95) != None:
            click(1170,990)
            print("Ziggs Store 4")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Poppy.png', confidence=0.95) != None:
            click(1170,990)
            print("Poppy Store 4")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Lulu.png', confidence=0.95) != None:
            click(1170,990)
            print("Lulu Store 4")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Corki.png', confidence=0.95) != None:
            click(1170,990)
            print("Corki Store 4")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Gnar.png', confidence=0.95) != None:
            click(1170,990)
            print("Gnar Store 4")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Vex.png', confidence=0.95) != None:
            click(1170,990)
            print("Vex Store 4")
            time.sleep(0.01)
        

    #Store 5
        pic = pyautogui.screenshot(region=(472,922,1011,158))
        width, height = pic.size #This saves the width & height of the variable "pic"
        if pyautogui.locateOnScreen('Ziggs.png', confidence=0.95) != None:
            click(1370,990)
            print("Ziggs Store 5")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Poppy.png', confidence=0.95) != None:
            click(1370,990)
            print("Poppy Store 5")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Lulu.png', confidence=0.95) != None:
            click(1370,990)
            print("Lulu Store 5")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Corki.png', confidence=0.95) != None:
            click(1370,990)
            print("Corki Store 5")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Gnar.png', confidence=0.95) != None:
            click(1370,990)
            print("Gnar Store 5")
            time.sleep(0.01)
            
        if pyautogui.locateOnScreen('Vex.png', confidence=0.95) != None:
            click(1370,990)
            print("Vex Store 5")
            time.sleep(0.01)


if keyboard.is_pressed('m'):
    print("Script deactivated")
