import pyautogui
import time
import pyscreeze

#pyautogui.typewrite("Hello, World!", interval=0.1)  # Type with a delay of 0.1 seconds between each character
#pyautogui.hotkey('cmdl', 'a')  # Select all text
#pyautogui.hotkey('cmd', 'c')  # Copy selected text 

screenshot = pyautogui.screenshot()
screenshot.save("final.png")  # Save the screenshot to a file