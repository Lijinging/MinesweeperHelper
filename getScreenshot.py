#coding:gbk
from PIL import ImageGrab
import pyautogui



def getPos(initPic1="img/left_up.png", initPic2="img/right_down.png"):
    pos = pyautogui.locateOnScreen(initPic1)
    if pos != None:
        posX, posY = pos[:2]
    else:
        print "ERROR"
        exit()

    pos = pyautogui.locateOnScreen(initPic2)
    if pos != None:
        posX_end, posY_end = pos[:2]
    else:
        print "ERROR"
        exit()

    return posX+3, posY+3, posX_end+3, posY_end+3
