import time
import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ALL_CODE import EMAIL

def create_video():
    
    pyautogui.hotkey('shift','tab')
    time.sleep(2)
    pyautogui.hotkey('shift','tab')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    print ("Create Video Done")

def Again_login():
    
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)

    

    time.sleep(1)
    pyautogui.press('enter')

    print("Again Login Done")
  
def relogin():

    EMAIL.retrieveemailfromfile



def login_window():
    
    time.sleep(1)
    textemail = pyperclip.paste()
    time.sleep(2)
    pyautogui.typewrite(textemail,interval=0.05)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)

    password="Rishabh@1335"
    pyautogui.typewrite(password,interval=0.01)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(15)

    print("Login Window done")

def bakwash():
    pyautogui.press('tab')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.5)

    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)

    time.sleep(0.5)
    pyautogui.press('enter')

def bakwash2():
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('i')
    time.sleep(0.3)
    pyautogui.press('enter')

    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')


def bakwash3():

    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('p')
    time.sleep(0.3)
    pyautogui.press('enter')

    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')

def bakwash4():
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('m')
    time.sleep(0.3)
    pyautogui.press('enter')

    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')

def bakwash5():
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('enter')

    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)

    pyautogui.press('enter')






print("Step 3 Done")