import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui


def MOUSEUPARJAYE():

    time.sleep(1)
    #the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Calculate the center coordinates
    center_x = screen_width // 2
    center_y = screen_height // 200000000000

    try:
        pyautogui.moveTo(center_x, center_y, duration=1)
        print(f"Moved mouse to center of the screen ({center_x}, {center_y})")
    except pyautogui.FailSafeException:
        print("Movement stopped because of the pyautogui 'fail-safe' feature.")

    time.sleep(1)












def navigate_to_did_and_login():
    # Path to your WebDriver executable
    driver_path = '/path/to/your/driver'  # Change this to your WebDriver's path

    # URL of the website
    url = 'https://studio.d-id.com/editor'

    service = webdriver.firefox.service.Service(driver_path)
    service.start()
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()


    # Open the website
    driver.get(url)
    time.sleep(3)
    pyautogui.hotkey("alt",'space')
    time.sleep(0.5)
    pyautogui.hotkey('f')

    try:
        # Wait for the element with class 'css-17z7dti' to be clickable
        add_element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-17z7dti"))
        )
        
        # Click on the 'ADD' button
        add_element.click()

        # Wait for the page to fully load (change the expected condition according to your requirements)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

     
        # Wait for the 'Sign up' link to be clickable
        signup_link = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'c11ad22cc') and text()='Sign up']"))
        )
        
        # Click on the 'Sign up' link
        signup_link.click()

        # Wait for the page to fully load (change the expected condition according to your requirements)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Continue with further actions
        
    except Exception as e:
        print("An error occurred:", str(e))
        # Handle exceptions here if needed

    # Close the browser window when done


