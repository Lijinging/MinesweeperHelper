#coding:utf-8

from PIL import ImageGrab
from PIL import ImageChops
from PIL import Image
import mouseclick
import random

'''
算法：
1   对每一个九宫格：
    UNKNOWN数量+FLAG数量与该中心块数字相等：标记(右键)所有UNKNOWN为FLAG
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

openList=[]

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

def updateData(posX, posY, posX_end, posY_end, data, size, space=16):
    im = ImageGrab.grab([posX, posY, posX_end, posY_end])
    for i in range(size[0]):
        for j in range(size[1]):

            pix = im.load()

            colorcode = myhex(pix[(i*space+pointList[0][0], j*space+pointList[0][1])])+\
                        myhex(pix[(i*space+pointList[1][0], j*space+pointList[1][1])])+\
                        myhex(pix[(i*space+pointList[2][0], j*space+pointList[2][1])])
            data[i][j]=dict[colorcode]
            if data[i][j]==MINE:
                exit()

def updateunandflag(data, unandflag, size):
    for i in range(size[0]):
        for j in range(size[1]):
            unandflag[i][j]=getNumOfUnAndFLag(data, i, j, size)

def showData(data, size):
    for i in range(size[1]):
        for j in range(size[0]):
            print "%3d" % data[j][i],
        print
    print "----------------------------------"


def getAround(data, x, y, size):
    return [(i, j) for i in xrange(x-1, x+2) for j in xrange(y-1, y+2) if \
             i >= 0 and i <size[0] and j >= 0 and j < size[1]]

def getNumOfUnAndFLag(data, x, y, size):
    slist = getAround(data, x, y, size)
    cnt = 0
    for it in slist:
        if data[it[0]][it[1]]==UNKNOWN or data[it[0]][it[1]]==FLAG:
            cnt = cnt+1
    return cnt

def getNumOfFlag(data, x, y, size):
    slist = getAround(data, x, y, size)
    cnt = 0
    for it in slist:
        if data[it[0]][it[1]]==FLAG:
            cnt = cnt+1
    return cnt

def flagAround(data, posX, posY, x, y, size, space=16): #对x y周围所有未点开区域标记
    slist = getAround(data, x, y, size)
    for it in slist:
        if data[it[0]][it[1]] == UNKNOWN and data[it[0]][it[1]] != FLAG:
            data[it[0]][it[1]] = FLAG
            mouseclick.clickRight(posX, posY, it[0], it[1])
            print "flag:", (y, x), (it[1], it[0])

def openAround(data, posX, posY, x, y, size, unandflag,space=16): #对x y周围所有未点开区域标记
    slist = getAround(data, x, y, size)
    for it in slist:
        if data[it[0]][it[1]] == UNKNOWN:
            openList.append(it)
            print it, "-->openlist"



def flagnext(data, unandflag, size, posX, posY):
    for i in range(size[0]):
        for j in range(size[1]):
            if data[i][j] == unandflag[i][j]:
                flagAround(data, posX, posY, i, j, size)


def analysisOpen(data, unandflag, size, posX, posY):
    for i in range(size[0]):
        for j in range(size[1]):
            if getNumOfFlag(data, i, j, size) == data[i][j] and unandflag[i][j]!=data[i][j]:
                openAround(data, posX, posY, i, j, size, unandflag)

def showdetail():
    print openList


def nextclick(data, unandflag, size, posX, posY, posX_end, posY_end):
    flagnext(data, unandflag, size, posX, posY)
    analysisOpen(data, unandflag, size, posX, posY)
    while len(openList)>0:
        it = openList.pop(0)
        while data[it[0]][it[1]]!=UNKNOWN:
            if(len(openList)>0):
                it = openList.pop(0)
            else:
                showdetail()
              #  raw_input()
                return
        print "open:",it
        data[it[0]][it[1]] = SAFE
        mouseclick.clickLeft(posX, posY, it[0], it[1])
        updateData(posX, posY, posX_end, posY_end, data, size)
        updateunandflag(data, unandflag, size)
        flagnext(data, unandflag, size, posX, posY)
        analysisOpen(data, unandflag, size, posX, posY)
    showdetail()
 #   raw_input()



   # opennext(data, unandflag, size, posX, posY)




