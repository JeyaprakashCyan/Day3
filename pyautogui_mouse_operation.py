import pyautogui
import time
time.sleep(3)  # Wait for 5 seconds before starting the operations
#pyautogui.moveTo(100, 100, duration=1)  # Move the mouse to (100, 100) over 1 second   
#pyautogui.click(100,100) 
#pyautogui.typewrite("Hello, World!", interval=0.1)  # Type with a delay of 0.1 seconds between each character
#pyautogui.doubleClick(100, 100)  # Double-click at (100, 100)



pyautogui.scroll(-1000)
time.sleep(1)
pyautogui.scroll(1000)