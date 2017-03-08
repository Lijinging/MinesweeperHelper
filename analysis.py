#coding:utf-8

from PIL import ImageGrab
from PIL import ImageChops
from PIL import Image

'''
算法：
1   对每一个九宫格：
    UNKNOWN数量+FLAG数量与该中心块数字相等：标记所有UNKNOWN为FLAG
2
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

def getNumOfUnAndFLag(data, pMine, x, y, n):
    cnt = 0
    if x>0 and x <n-1 and y>0 and y<n-1:    #中心情况
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if data[i][j]==UNKNOWN or data[i][j]==FLAG:
                    cnt=cnt+1
    elif x==0 and y>0 and y<n-1:    #最左排非四角
        for j in range(y-1, y+2):
            if data[0][j]==UNKNOWN or data[0][j]==FLAG:
                cnt=cnt+1
    elif x==n-1 and y>0 and y<n-1:  #最右排非四角
        for j in range(y-1, y+2):
            if data[n-1][j]==UNKNOWN or data[n-1][j]==FLAG:
                cnt=cnt+1
    elif x>0 and x <n-1 and y==0:    #最上排非四角
        for i in range(x-1, x+2):
            if data[i][0]==UNKNOWN or data[i][0]==FLAG:
                cnt=cnt+1
    elif x>0 and x <n-1 and y==n-1:    #最下排非四角
        for i in range(x-1, x+2):
            if data[i][n-1]==UNKNOWN or data[i][n-1]==FLAG:
                cnt=cnt+1
    else:
        if data[0][0]==UNKNOWN or data[0][0]==FLAG:
            cnt=cnt+1
        if data[0][n-1]==UNKNOWN or data[0][n-1]==FLAG:
            cnt=cnt+1
        if data[n-1][0]==UNKNOWN or data[n-1][0]==FLAG:
            cnt=cnt+1
        if data[n-1][n-1]==UNKNOWN or data[n-1][n-1]==FLAG:
            cnt=cnt+1

