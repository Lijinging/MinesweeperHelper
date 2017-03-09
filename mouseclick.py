#coding:utf-8
import pyautogui

UNKNOWN = -1
MINE = -2
SAFE = 0
FLAG = -3

pyautogui.PAUSE = 0.001

def clickLeft(posX, posY, row, col, space=16):
    pyautogui.click(posX+(row+0.5)*space, posY+(col+0.5)*space)

def clickRight(posX, posY, row, col, space=16):
    pyautogui.rightClick(posX + (row + 0.5) * space, posY + (col + 0.5) * space)

def clickLeftAndRight(posX, posY, row, col, space=16):
    pyautogui.mouseDown(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "left")
    pyautogui.mouseDown(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "right")
    pyautogui.mouseUp(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "left")
    pyautogui.mouseUp(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "right")

def flag(data, posX, posY, x, y, space=16):
    if data[x][y] != UNKNOWN:
        return
    data[x][y] = FLAG
    clickRight(posX, posY, x, y, space)

def click(data, posX, posY, x, y, space=16):
    if data[x][y] != UNKNOWN:
        return
    clickLeft()





