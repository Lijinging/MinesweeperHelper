#coding:utf-8
import getScreenshot
import mouseclick
from PIL import ImageGrab
from PIL import ImageChops
from PIL import Image
import random

'''
1 截图
2 获取指定区域截图
3 识别扫雷区域
4 运算
5 点击
'''

UNKNOWN = -1
MINE = -2
SAFE = 0
FLAG = -3

filenameList=["img/1.PNG",
              "img/2.PNG",
              "img/3.PNG",
              "img/4.PNG",
              "img/5.PNG",
              "img/6.PNG",
              "img/7.PNG",
              "img/8.PNG"]

flagfilename="img/flag.PNG"
safefilename="img/safe.PNG"
unknownfilename="img/unknown.PNG"

minefilenameList=["img/mine1.PNG",
                  "img/mine2.PNG"]

def showData(data, n):
    for i in range(n):
        for j in range(n):
            print data[j][i],
        print "\n"
    print "-----------------"

def isEqual(im1, filepath):
    im2 = Image.open(filepath)
    a = ImageChops.difference(im1, im2)
    if ImageChops.difference(im1, im2).getbbox() is None:
        return True
    else:
        return False

def isEqualOneOf(im, imlist):
    for im2 in imlist:
        if isEqual(im, im2):
            return True
    return False


def updateData(posX, posY, data, n, space=16):
    for i in range(n):
        for j in range(n):
            im = ImageGrab.grab([posX+i*space, posY+j*space, posX+(i+1)*space, posY+(j+1)*space])
        #    im.show()
            if isEqualOneOf(im, minefilenameList):
                exit()
            if isEqual(im, safefilename):
                data[i][j] = SAFE
                continue
            if isEqual(im, flagfilename):
                data[i][j] = FLAG
                continue
            if isEqual(im, unknownfilename):
                data[i][j] = UNKNOWN
                continue
            for k in range(1,9):
                if isEqual(im, "img/"+str(k)+".PNG"):
                    data[i][j] = k

def updateData(x, y, data, n, space=16):
    for i in range(n):
        for j in range(n):
            im = ImageGrab.grab([x+i*space, y+j*space, x+(i+1)*space, y+(j+1)*space])
        #    im.show()
            if isEqualOneOf(im, minefilenameList):
                exit()
            if isEqual(im, safefilename):
                data[i][j] = SAFE
                continue
            if isEqual(im, flagfilename):
                data[i][j] = FLAG
                continue
            if isEqual(im, unknownfilename):
                data[i][j] = UNKNOWN
                continue
            for k in range(1,9):
                if isEqual(im, "img/"+str(k)+".PNG"):
                    data[i][j] = k


if __name__ == '__main__':
    posX, posY, posX_end, posY_end = getScreenshot.getPos()
    n = (posX_end-posX)/16
    data = [[UNKNOWN for i in range(n)] for i in range(n)]
    pMine = [[50 for i in range(n)] for i in range(n)]
    hasEnd = False
    mouseclick.clickLeft(posX, posY, random.randint(0, n-1), random.randint(0, n-1))
    while not hasEnd:
        updateData(posX, posY, data, n)
        showData(data, n)
        mouseclick.clickLeft(posX, posY, random.randint(0, n-1), random.randint(0, n-1))

    mouseclick.clickLeft(posX, posY, 5, 6)
