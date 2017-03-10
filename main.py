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
    size = [(posX_end-posX)/16, (posY_end-posY)/16]
    data = [[UNKNOWN for i in range(size[1])] for j in range(size[0])]
    unandflag = [[9 for i in range(size[1])] for j in range(size[0])]
    pMine = [[50 for i in range(size[1])] for j in range(size[0])]
    hasEnd = False

    while not hasEnd:

        it = analysis.speculate(data, size)
        mouseclick.clickLeft(posX, posY, it[0], it[1])
        analysis.updateData(posX, posY, posX_end, posY_end, data, size)
        analysis.updateunandflag(data, unandflag, size)

        #analysis.showData(data, size)
        #analysis.showData(unandflag, size)
        analysis.nextclick(data, unandflag, size, posX, posY, posX_end, posY_end)
    #    mouseclick.clickLeft(posX, posY, random.randint(0, size[0]-1), random.randint(0, size[1]-1))
     #   raw_input()

  #  mouseclick.clickLeft(posX, posY, 5, 6)
