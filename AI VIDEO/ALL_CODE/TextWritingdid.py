import time
import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time


def retrievematerialfromfiletorename():
    file_pathofmaterial = 'ALL_CODE/ChatGpttext/material.txt'
    
# Later, retrieve the email from the stored file
    with open(file_pathofmaterial, 'r') as file:
        stored_textmaterial = file.read()
        pyperclip.copy(stored_textmaterial)
        print(f"Retrieved email '{stored_textmaterial}' from '{file_pathofmaterial}'")




def click_on_screen(x, y):
    time.sleep(5)
    subprocess.run(['xdotool', 'mousemove', str(x), str(y), 'click', '1'])



def writing():
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    print("Writing Done")
    pyautogui.press('enter')


def VoiceSelection():
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

    pyautogui.typewrite("Ashley",interval=0.01)
    pyautogui.press('enter')
    time.sleep(5)


def Generatevideoparclick(x,y):
    subprocess.run(['xdotool', 'mousemove', str(x), str(y), 'click', '1'])

    

def patanahikyahai():

    time.sleep(10)
    pyautogui.hotkey('shift','tab')  
    pyautogui.press('enter')


def VideoGenerate():
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(70)

