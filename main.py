import pyautogui as pygui
import keyboard
import time

res = 5
cells = []
def createCells():
    fx = ((x2 - x1) / res)
    fy = ((y2 - y1) / res)
    
    for yi in range(res + 1):
        if yi != 0:
            for xi in range(res + 1):
                if xi != 0:
                    tp = ((fx*(xi-1))+x1, (fy*(yi-1))+y1)
                    bp = ((fx*xi)+x1, (fy*yi)+y1)

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
        createCells()
        cellDraw(cells[4])
        print(len(cells))
        print('done')
        break

