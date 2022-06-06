from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#https://www.agame.com/game/magic-piano-tiles

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print("Script Active")

while keyboard.is_pressed('`') == False:
    if pyautogui.pixel(570, 500)[0] == 0:
        click(570, 500)
    if pyautogui.pixel(650, 500)[0] == 0:
        click(650, 500)
    if pyautogui.pixel(730, 500)[0] == 0:
        click(730, 500)
    if pyautogui.pixel(810, 500)[0] == 0:
        click(810, 500)
        
if keyboard.is_pressed('`'):
    print("Script deactivated")
