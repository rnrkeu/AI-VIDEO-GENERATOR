import time
import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time


def clickonscreenagain(x,y):
    
    subprocess.run(['xdotool', 'mousemove', str(x), str(y), 'click', '1'])

def retrievetitlefromfiletorename():
    file_pathoftitle = "ALL_CODE/ChatGpttext/title.txt"
# Later, retrieve the email from the stored file
    with open(file_pathoftitle, 'r') as file:
        stored_texttile = file.read()
        pyperclip.copy(stored_texttile)
        print(f"Retrieved email '{stored_texttile}' from '{file_pathoftitle}'")

def RenameVideo():
    time.sleep(0.3)
    pyautogui.press('tab')
    pyautogui.hotkey('backspace')
    time.sleep(0.3)
    pyautogui.hotkey("ctrl",'v')

def DownladVideo():
    time.sleep(5)
    pyautogui.hotkey('shift','tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')

def Ending_all_Task():
    time.sleep(10)
    pyautogui.hotkey("ctrl",'shift','w')

    pyautogui.hotkey("ctrl",'shift','w')

    pyautogui.hotkey("ctrl",'shift','w')

    pyautogui.hotkey("ctrl",'shift','w')


#def DeletingVideo():

    



    
