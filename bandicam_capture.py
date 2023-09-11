import pyautogui as pg
import keyboard as kb
import time

print('start')

while True :
    if kb.is_pressed('esc') :
        print("end")
        break

    else :
        
        pg.moveTo(205, 72)
        pg.click()
        
        ##pg.moveTo(1381, 741)
        pg.moveTo(1200, 721)
        pg.click()

        time.sleep(2)
       

## 캡처위치 198 76
## 화살표 위치 1244 712 <-교보 / 1257 725 <- yes24  