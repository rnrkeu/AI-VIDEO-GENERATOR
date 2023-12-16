
import pyautogui
import time

def Move_mousetocentre():
    time.sleep(1)
    #the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Calculate the center coordinates
    center_x = screen_width // 2
    center_y = screen_height // 2

    try:
        pyautogui.moveTo(center_x, center_y, duration=1)
        print(f"Moved mouse to center of the screen ({center_x}, {center_y})")
    except pyautogui.FailSafeException:
        print("Movement stopped because of the pyautogui 'fail-safe' feature.")

    time.sleep(1)

def move_mousetoclickablezone():
    # Replace these coordinates with your desired x and y values
    target_x = 1573
    target_y = 500

    try:
        pyautogui.moveTo(target_x, target_y, duration=1)
        print(f"Moved mouse to ({target_x}, {target_y})")
    except pyautogui.FailSafeException:
        print("Movement stopped because of the pyautogui 'fail-safe' feature.")


