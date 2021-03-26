import pyautogui as auto
import time

comment = "Teste"


class Search:
    def __init__(self, msg):
        auto.moveTo(172, 749)
        auto.click()
        auto.typewrite('google chrome')
        auto.press('enter')

        time.sleep(2)

        auto.moveTo(321, 51)
        auto.click()
        auto.typewrite('youtube.com')
        auto.press('enter')

        time.sleep(2)

        auto.moveTo(379, 101)
        auto.click()
        auto.typewrite('Imersao ao Infinito')
        auto.press('enter')

        time.sleep(2)

        auto.moveTo(444, 249, 1)
        auto.click()

        time.sleep(2)

        auto.moveTo(512, 430, 1)
        auto.click()
        auto.moveTo(366, 584, 1)
        auto.click()

        time.sleep(3)

        auto.scroll(-500)

        auto.moveTo(131, 570, 1)
        auto.click()
        auto.typewrite(msg)

        auto.moveTo(834, 614, 1)
        auto.click()

        auto.moveTo(1343, 12, 2)
        auto.click()


auto_objy = Search(comment)
