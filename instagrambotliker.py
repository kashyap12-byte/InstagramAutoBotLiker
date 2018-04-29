# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:27:33 2018
@author: dms24081999
"""
# works with Half-opened Google Chrome towards left of the screen
#resolution needed is 1920*1080
import pyautogui
import time
print(pyautogui.size())
print("current location:",pyautogui.position())
print("Open any instagram user page")
print("Enter Number of Posts:")
count=input()
count=int(count)+1
print("Program will Execute " + str(count) + " number of times")
print("Hold Ctrl+Alt+Del to force exit the program in progress")
for y in range (0,int(count)):
    pyautogui.click(296,577,clicks=2)
    time.sleep(.600)    
    pyautogui.click(923,574,clicks=1)
    time.sleep(.600)
print("Task Completed")
raw_input() #"Enter" key to exit program, used in pyinstaller module
            #Its not an error, it holds console output window

#Advantages:
#1.Automate liking users post with mouse clicks
#2.Saves time and energy for studying

#Drawbacks:
#1.This Bot cannot like a video since the middle screen of the video contains 
#  Pause and Play Video controls
#2.It works on a user_name page eg:https://instagram.com/username,
#  it doesn't work on https://instagram.com, it needs a user_name page