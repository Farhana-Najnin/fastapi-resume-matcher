import pyautogui
from time import sleep
sleep(3)
pyautogui.write('hello!',interval=.25)
pyautogui.press('enter')
for i in range(0,3):
    pyautogui.write('I love you , Python',interval=0.25)
    pyautogui.press('enter') 
    