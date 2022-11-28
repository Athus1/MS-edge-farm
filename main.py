import pyautogui
import time
import string
import random
import subprocess


def desktopsearch():
    x = 34
    a = 10
    string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    time.sleep(5)
    while x > 0:
        pyautogui.hotkey("ctrl", "t", _pause=0.001)
        while a > 0:
            pyautogui.write(random.choice(string.ascii_letters), _pause=0.001)
            a = a - 1
        pyautogui.press("enter", _pause=0.001)
        x = x - 1
        a = 10

        time.sleep(0.1)


def mobilesearch():
    string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = 5
    c = 20

    time.sleep(5)
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("bing.com")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("f12")
    time.sleep(2)
    # IF NEEDED ADD ABSOLUTE PATH OF IMAGE IN THE LINE BELOW
    button7location = pyautogui.locateOnScreen(r'C:\Users\athar\PycharmProjects\MS-edge-farming-main\searchfind.png')
    print(button7location)
    button7point = pyautogui.center(button7location)
    button7x, button7y = button7point
    pyautogui.click(button7x, button7y)

    pyautogui.write("hello")

    pyautogui.press("enter")
    time.sleep(2)

    pyautogui.write("hello")

    pyautogui.press("enter")
    time.sleep(2)

    while c > 0:
        button2location = pyautogui.locateOnScreen(r'C:\Users\athar\PycharmProjects\MS-edge-farming-main\searchfind.png')
        print(button2location)
        button2point = pyautogui.center(button2location)
        button2x, button2y = button2point
        button2x = button2x - 150
        pyautogui.click(button2x, button2y)
        while b > 0:
            pyautogui.write(random.choice(string.ascii_letters))
            b = b - 1
        pyautogui.press("enter")
        c = c - 1
        print(c)
        time.sleep(0.3)
        b = 5


subprocess.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

desktopsearch()

mobilesearch()
