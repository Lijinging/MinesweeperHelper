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

pointList=[(11,11),(1,1),(3,3)]

dict={}
dict["0000ffc0c0c0c0c0c0"]=1
dict["008000c0c0c0c0c0c0"]=2
dict["ff0000c0c0c0ff0000"]=3
dict["000080c0c0c0c0c0c0"]=4
dict["800000c0c0c0800000"]=5
dict["008080c0c0c0c0c0c0"]=6
dict["c0c0c0c0c0c0000000"]=7
dict["808080c0c0c0c0c0c0"]=8
dict["000000ffffffc0c0c0"]=FLAG
dict["c0c0c0c0c0c0c0c0c0"]=SAFE
dict["c0c0c0ffffffc0c0c0"]=UNKNOWN
dict["000000c0c0c0c0c0c0"]=MINE
dict["000000ff0000ff0000"]=MINE

myhex = lambda x: '%02x%02x%02x'% x

def updateData(posX, posY, posX_end, posY_end, data, n, space=16):
    im = ImageGrab.grab([posX, posY, posX_end, posY_end])
    for i in range(n):
        for j in range(n):

            pix = im.load()

            colorcode = myhex(pix[(i*space+pointList[0][0], j*space+pointList[0][1])])+\
                        myhex(pix[(i*space+pointList[1][0], j*space+pointList[1][1])])+\
                        myhex(pix[(i*space+pointList[2][0], j*space+pointList[2][1])])
            data[i][j]=dict[colorcode]

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

