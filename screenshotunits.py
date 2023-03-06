from tkinter import *
from PIL import ImageTk, Image
import pyautogui

main = Tk()
main.title("Screenshot GUI")

Imagename2 = str("vvv")


def screen_1():
    iml = pyautogui.screenshot(region=(480, 928, 192, 143))
    scname1 = Screenshot_1_imagelabel.get()
    new_loc1 = "C:\Python\TFT Bot Intermediate Image\Set 8\\" + str(scname1) + ".png"
    iml.save(r"" + new_loc1)

def screen_2():
    iml = pyautogui.screenshot(region=(681, 928, 192, 143))
    scname2 = Screenshot_2_imagelabel.get()
    new_loc2 = "C:\Python\TFT Bot Intermediate Image\Set 8\\" + str(scname2) + ".png"
    iml.save(r"" + new_loc2)


def screen_3():
    iml = pyautogui.screenshot(region=(882, 928, 192, 143))
    scname3 = Screenshot_3_imagelabel.get()
    new_loc3 = "C:\Python\TFT Bot Intermediate Image\Set 8\\" + str(scname3) + ".png"
    iml.save(r"" + new_loc3)

def screen_4():
    iml = pyautogui.screenshot(region=(1084, 928, 192, 143))
    scname4 = Screenshot_4_imagelabel.get()
    new_loc4 = "C:\Python\TFT Bot Intermediate Image\Set 8\\" + str(scname4) + ".png"
    iml.save(r"" + new_loc4)

def screen_5():
    iml = pyautogui.screenshot(region=(1285, 928, 192, 143))
    scname5 = Screenshot_5_imagelabel.get()
    new_loc5 = "C:\Python\TFT Bot Intermediate Image\Set 8\\" + str(scname5) + ".png"
    iml.save(r"" + new_loc5)


# objects
Screenshot_1_imagelabel = Entry(main, width=50, borderwidth=5)
Screenshot_2_imagelabel = Entry(main, width=50, borderwidth=5)
Screenshot_3_imagelabel = Entry(main, width=50, borderwidth=5)
Screenshot_4_imagelabel = Entry(main, width=50, borderwidth=5)
Screenshot_5_imagelabel = Entry(main, width=50, borderwidth=5)


Screenshot_1_button = Button(main, text="Screenshot 1", command=screen_1)
Screenshot_2_button = Button(main, text="Screenshot 2", command=screen_2)
Screenshot_3_button = Button(main, text="Screenshot 3", command=screen_3)
Screenshot_4_button = Button(main, text="Screenshot 4", command=screen_4)
Screenshot_5_button = Button(main, text="Screenshot 5", command=screen_5)

# placement
Screenshot_1_imagelabel.grid(row=0, column=0, columnspan=2)
Screenshot_2_imagelabel.grid(row=1, column=0, columnspan=2)
Screenshot_3_imagelabel.grid(row=2, column=0, columnspan=2)
Screenshot_4_imagelabel.grid(row=3, column=0, columnspan=2)
Screenshot_5_imagelabel.grid(row=4, column=0, columnspan=2)

Screenshot_1_button.grid(row=0, column=2)
Screenshot_2_button.grid(row=1, column=2)
Screenshot_3_button.grid(row=2, column=2)
Screenshot_4_button.grid(row=3, column=2)
Screenshot_5_button.grid(row=4, column=2)


main.mainloop()
