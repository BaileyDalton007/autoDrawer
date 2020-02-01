import pyautogui as pygui
import keyboard
import time


def drawX():

    pygui.moveTo(x1, y1)
    pygui.dragTo(x2,y2)
    pygui.moveTo(x1, y2)
    pygui.dragTo(x2, y1)


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
        drawX()
        print('done')
        break

