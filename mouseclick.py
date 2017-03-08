#coding:utf-8
import pyautogui

pyautogui.PAUSE = 0.01

def clickLeft(posX, posY, row, col, space=16):
    pyautogui.click(posX+(row+0.5)*space, posY+(col+0.5)*space)

def clickRight(posX, posY, row, col, space=16):
    pyautogui.rightClick(posX + (row + 0.5) * space, posY + (col + 0.5) * space)

def clickLeftAndRight(posX, posY, row, col, space=16):
    pyautogui.mouseDown(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "left")
    pyautogui.mouseDown(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "right")
    pyautogui.mouseUp(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "left")
    pyautogui.mouseUp(posX + (row + 0.5) * space, posY + (col + 0.5) * space, "right")