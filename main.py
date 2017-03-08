#coding:utf-8
import getScreenshot
import mouseclick
import analysis

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

if __name__ == '__main__':
    posX, posY, posX_end, posY_end = getScreenshot.getPos()
    n = (posX_end-posX)/16
    data = [[UNKNOWN for i in range(n)] for i in range(n)]
    pMine = [[50 for i in range(n)] for i in range(n)]
    hasEnd = False
    mouseclick.clickLeft(posX, posY, random.randint(0, n-1), random.randint(0, n-1))
    while not hasEnd:
        analysis.updateData(posX, posY, data, n)
        analysis.showData(data, n)
        mouseclick.clickLeft(posX, posY, random.randint(0, n-1), random.randint(0, n-1))

    mouseclick.clickLeft(posX, posY, 5, 6)
