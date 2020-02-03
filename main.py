import pyautogui as pygui
from PIL import Image
import pyscreenshot
import keyboard
import time
from stopwatch import Stopwatch

res = 100
canvasCells = []
imageCells = []
cellImageData = []
testPoints = []
drawPoints = []

def createCells(px1, py1, px2, py2, cells):
    fx = ((px2 - px1) / res)
    fy = ((py2 - py1) / res)
    
    for yi in range(res + 1):
        if yi != 0:
            for xi in range(res + 1):
                if xi != 0:
                    tp = ((fx*(xi-1))+px1, (fy*(yi-1))+py1)
                    bp = ((fx*xi)+px1, (fy*yi)+py1)

                    cells.append([tp, bp])

def cellMap():
    fx = ((x2 - x1) / res)
    fy = ((y2 - y1) / res)
    for yi in range(res + 1):
        if yi != 0:
            for xi in range(res + 1):
                if xi != 0:
                    pygui.moveTo((fx*(xi-1))+x1, (fy*(yi-1))+y1)
                    pygui.dragTo((fx*(xi-1))+x1, (fy*yi)+y1)
                    pygui.dragTo((fx*xi)+x1, (fy*yi)+y1)
                    pygui.dragTo((fx*xi)+x1, (fy*(yi-1))+y1)
                    pygui.dragTo((fx*(xi-1))+x1, (fy*(yi-1))+y1)
    pygui.moveTo(x2, y2)

def cellDraw(cell):
    cx1, cy1 = cell[0]
    cx2, cy2 = cell[1]
    pygui.moveTo(cx1, cy1)
    pygui.dragTo(cx1, cy2)
    pygui.dragTo(cx2, cy2)
    pygui.dragTo(cx2, cy1)
    pygui.dragTo(cx1, cy1)

def drawDarkPixels(rgb, testPoints, drawPoints):
    for i in range(len(testPoints)):
        rgbtup = rgb[i]
        r = rgbtup[0]
        g = rgbtup[1]
        b = rgbtup[2]
        if r < 100 and g < 100 and b < 100:
            pygui.moveTo(drawPoints[i])
            pygui.click()

def makeTestPoints():
    createCells(ix1, iy1, ix2, iy2, imageCells)
    for i in range(len(imageCells)):
        tx1, ty1 = (imageCells[i][0][0], imageCells[i][0][1])
        tx2, ty2 = (imageCells[i][1][0], imageCells[i][1][1])
        testPoint = (round(((tx2-tx1)/2)+tx1, 5), round(((ty2-ty1)/2)+ty1, 5))
        testPoints.append(testPoint)
    return testPoints

def makeDrawPoints():
    createCells(x1, y1, x2, y2, canvasCells)
    for i in range(len(canvasCells)):
        tx1, ty1 = (canvasCells[i][0][0], canvasCells[i][0][1])
        tx2, ty2 = (canvasCells[i][1][0], canvasCells[i][1][1])
        point = (round(((tx2-tx1)/2)+tx1, 5), round(((ty2-ty1)/2)+ty1, 5))
        drawPoints.append(point)
    return drawPoints

def getImageData(testPoints):
    input = im.load()
    data = []
    for i in range(len(testPoints)):
        data.append(input[testPoints[i]])
    return data

while True:
    if keyboard.is_pressed('c'):
        ix1, iy1 = pygui.position()
        print(ix1, iy1)
        break

time.sleep(1)

while True:
    if keyboard.is_pressed('c'):
        ix2, iy2 = pygui.position()
        im = pygui.screenshot()
        #im.show()
        print(ix2, iy2)
        makeTestPoints()
        cellImageData = getImageData(testPoints)
        break


while True:
    if keyboard.is_pressed('x'):
        x1, y1 = pygui.position()
        print(x1, y1)
        break
    
time.sleep(1)

while True:
    if keyboard.is_pressed('x'):
        x2, y2 = pygui.position()
        print(x2, y2)
        break

while True:
    if keyboard.is_pressed('z'):
        stopwatch = Stopwatch()
        makeDrawPoints()
        drawDarkPixels(cellImageData, testPoints, drawPoints)
        print('done')
        stopwatch.stop()
        print(str(stopwatch))
        break

