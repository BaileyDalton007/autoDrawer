import pyautogui as pygui
import keyboard

while True:
    try:
        if keyboard.is_pressed('x'):
            print("hi")
            break
    except:
        break