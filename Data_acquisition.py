# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 22:48:19 2020

@author: Daniel
"""

import numpy as np
import tensorflow as tf
import cv2 as cv2
import time
# import pyautogui
from PIL import ImageGrab
import win32gui
import keyboard

width = 800
height = 500
record = False
recorded = 0
path = "image_data"


while True:
    handle = win32gui.FindWindow(None,"Brawlhalla")
    win32gui.SetWindowPos(handle, None, 1920-width,10,width,height, 0)
    img = ImageGrab.grab(bbox=(1920-width,10,1920,10+height))
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", img_np)
    if record:
        cv2.imwrite(path+"/image"+str(recorded)+".jpg", frame)
        print("Recorded")
        recorded+=1
        
    k = cv2.waitKey(20) & 0xff
    if k == 27: #stop with esc
        break
    elif k == 99: #stop with "c"
        k = cv2.waitKey(0) & 0xff
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("q"):
        break
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("s"):
        record = not record
        print("Pressed")
    
cv2.destroyAllWindows()