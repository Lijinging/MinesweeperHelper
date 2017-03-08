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

UNKNOWN = 0
MINE    = -2
SAFE    = -1
FLAG    = -3

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
    print "------------"

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


def updateData(data, n, space=16):
    for i in range(n):
        for j in range(n):
            im = ImageGrab.grab([x+i*space, y+j*space, x+(i+1)*space, y+(j+1)*space])
        #    im.show()
            if isEqualOneOf(im, minefilenameList):
                exit()
            if isEqual(im, safefilename):
                data[i][j]=SAFE
                continue
            if isEqual(im, flagfilename):
                data[i][j]=FLAG
                continue
            if isEqual(im, unknownfilename):
                data[i][j]=UNKNOWN
                continue
            for k in range(1,9):
                if isEqual(im, "img/"+str(k)+".PNG"):
                    data[i][j] = k


if __name__ == '__main__':
    x, y, x_end, y_end = getScreenshot.getPos()
    n = (x_end-x)/16
    data = [[-10 for i in range(n)] for i in range(n)]
    pMine = [[50 for i in range(n)] for i in range(n)]
    hasEnd = False
    mouseclick.clickLeft(x, y, random.randint(0,n-1), random.randint(0,n-1))
    while not hasEnd:
        updateData(data, n)
        showData(data, n)
        mouseclick.clickLeft(x, y, random.randint(0, n-1), random.randint(0, n-1))


    mouseclick.clickLeft(x, y, 5, 6)
