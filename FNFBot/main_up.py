import cv2 as cv
import numpy as np
import keyboard
import pydirectinput
from windowcapture_up import WindowCapture
print("Press Q to stop")

pydirectinput.PAUSE = 0.0001

windowname = "Roblox"

# initialize the WindowCapture class
wincap = WindowCapture(windowname)


#Start Window Capture thrread.s
wincap.start()

def left_control(putithere):

    #All the visual processing
    hsv_frame = cv.cvtColor(putithere, cv.COLOR_BGR2HSV)
        
    low = np.array([50, 230, 200])
    high = np.array([70, 255 ,255])
    mask = cv.inRange(hsv_frame, low, high)
        
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv.contourArea(x), reverse=True)
    
    if contours:
        pydirectinput.keyDown("w")
    elif keyboard.is_pressed("t"):
        pydirectinput.keyDown("w")
    else:
        pydirectinput.keyUp("w")

    return putithere

#Communicator
while(True):

    # if we don't have a screenshot yet, don't run the code below this point yet
    if wincap.screenshot is None:
        continue

    video = left_control(wincap.screenshot)

    #esfSend captured screenshot  to mousecontrol.py
    cv.imshow("Name", video)
    
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if keyboard.is_pressed('q'):
        print("Shutting down")
        wincap.stop()
        cv.destroyAllWindows()
        break

