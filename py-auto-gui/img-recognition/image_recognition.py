import pyautogui as pyag
import time

while True:
    x = pyag.locateAllOnScreen('star.png', confidence=0.976)
    time.sleep(2)
    i = 0
    for each in list(x):
        print(i)
        i += 1
        each = pyag.center(each)
        place = list(each)
        x = place[0]
        y = place[1]
        pyag.moveTo(x, y)
        print("Star found")
        time.sleep(2)
