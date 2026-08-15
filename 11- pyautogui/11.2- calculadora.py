import pyautogui
import time
pyautogui.click(800,1050)
pyautogui.typewrite("calculadora",interval=0.1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("8")
pyautogui.press("+")
pyautogui.press("2")
pyautogui.press("=")