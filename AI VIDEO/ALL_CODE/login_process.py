import time
import pyperclip
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ALL_CODE import EMAIL

def newprocess():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(3)
    pyautogui.typewrite("Rishabh@1335", interval=0.01)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.hotkey("alt", 'tab')
    time.sleep(1)

def emailprocess():
    time.sleep(10)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    text2 = "https://www.fakemail.net/window/id/2"
    pyautogui.typewrite(text2, interval=0.01)
    pyautogui.hotkey('enter')
    time.sleep(5)

def extract_and_copy_email():
    # Path to your WebDriver executable
    driver_path = '/path/to/your/driver'  # Change this to your WebDriver's path

    # URL of the website
    url = 'https://www.fakemail.net'  # Replace with your URL

    service = webdriver.firefox.service.Service(driver_path)
    service.start()
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    time.sleep(3)
    pyautogui.hotkey("alt",'space')
    time.sleep(0.5)
    pyautogui.hotkey('f')
    
    # Open the website
    driver.get(url)

    try:
        # Wait for the element with ID 'email' to be visible
        email_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )

        # Extract text from the 'email' element
        email_text = email_element.text
        print("Email text:", email_text)

        # Copy text to clipboard
        pyperclip.copy(email_text)
        print("Email text copied to clipboard.")
        EMAIL.savingemailtofile
        

        # Wait for the page to fully load (change the expected condition according to your requirements)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        

        # Continue with further actions
        
    except Exception as e:
        print("An error occurred:", str(e))
        # Handle exceptions here if needed
        time.sleep(10)



def confirmbuttonclick():
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
    time.sleep(10)

    


