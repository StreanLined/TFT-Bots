# TFT-Bots Set 6.5
Bots for TFT to learn
[Python]

Modules
pyautogui
win32api/win32con
-"object detection"
-"mss for locate on screen"
-"mouse/pynput to move the mouse"

__TFT Bot Intermediate Image V1.0.0.py__
Does not work. Iteration V1 and concept idea.

# TFT-Bots Set 7
Skipped

# TFT-Bots Set 8
Created script to take screenshots of champion cards
Named: screenshotunts
file dump location: C:\Python\TFT Bot Intermediate Image\Set 8\

Entry fields for ease-of-use renaming of .png files
Champion card sizes have been standardized.

__TFT auto-buy Set 8__
Working script that buys Units using * *pyautogui.locateOnScreen* *
Up to 9 different units can be selected from the Cost-Dropdown boxes.
Selected units can be reset with the reset button; must also select which row should be reset.
"Toggle" button to activate once units have been selected.
"Esc" key to re-open GUI. __NOTE:__ Selected units will be reset.

__Libraries used:__
* *PyAutogui, TkInter, PIL, Keyboard*

Future plans:
- [ ] Add trait button as an alternative to cost dropdown (Variables already set up)
- [ ] Script continues to run when bench is full [Needs an urgent fix!]
- [ ] ~Maybe make the GUI look nicer
- [ ] ~Maybe find an alternative GUI library (loops do not work with TkInter as it has its own constant loop)

__Bugs__
- [ ] "Esc" key doesn't register once a unit has been bought by the script
