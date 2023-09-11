import pyautogui as pg
import keyboard as kb
import time

## 매크로 시작 출력
print('start')

## 무한루프
while True :

    if kb.is_pressed('esc') :
        print("end")
        break

    else :
        
        pg.moveTo(205, 72)
        pg.click()
        
        pg.moveTo(1200, 721)
        pg.click()

        time.sleep(2)
       
