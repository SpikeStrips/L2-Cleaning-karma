from ahk import AHK
import time
import pyautogui
from PIL import Image

ahk = AHK()

def NPS_ClanHall():
    time.sleep(2)
    ahk.key_down('1')
    time.sleep(1)
    ahk.key_up('1')

    time.sleep(2)
    button1location = pyautogui.locateOnScreen('01.png', confidence=0.9)
    time.sleep(1)
    pyautogui.moveTo(button1location[0], button1location[1], 0.2)
    pyautogui.mouseDown(); pyautogui.mouseUp()
    time.sleep(2)
    button2location = pyautogui.locateOnScreen('02.png', confidence=0.9)
    time.sleep(1)
    pyautogui.moveTo(button2location[0], button2location[1], 0.2)
    pyautogui.mouseDown(); pyautogui.mouseUp()
    time.sleep(2)
    button3location = pyautogui.locateOnScreen('03.png', confidence=0.9)
    time.sleep(1)
    pyautogui.moveTo(button3location[0], button3location[1], 0.2)
    pyautogui.mouseDown(); pyautogui.mouseUp()
    time.sleep(2)
    ahk.key_down('2')
    time.sleep(1)
    ahk.key_up('2')
    time.sleep(10)
    button4location = pyautogui.locateOnScreen('04.png', confidence=0.9)
    time.sleep(1)
    pyautogui.moveTo(button4location[0], button4location[1], 0.2)
    pyautogui.mouseDown(); pyautogui.mouseUp()

while True:
    NPS_ClanHall()
