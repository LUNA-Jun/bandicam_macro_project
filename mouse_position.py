import pyautogui as pg
import keyboard as kb
import time

pg.PAUSE = 1
pg.FAILSAFE = True

print('start')

while True :
    if kb.is_pressed('esc') :
        print("end")
        break

    else :
        print("Position : ", pg.position())
        time.sleep(3)