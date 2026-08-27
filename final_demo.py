import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE=True
pyautogui.PAUSE=1.0

print("Open the chrome browser...")
time.sleep(1)

pyautogui.hotkey('win','r',interval=0.1)  # Open the Run dialog
time.sleep(1)
pyautogui.write('chrome', interval=0.15)  # Type 'chrome' to open Google Chrome
time.sleep(1)
pyautogui.press('enter')  # Press Enter to open Chrome
time.sleep(3)  # Wait for Chrome to open

print("Navigating to the website...")
pyautogui.hotkey('ctrl','t',interval=0.1)  # Focus on the address bar
pyautogui.write('https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108?type=locality&city=bengaluru', interval=0.15)  # Type the URL
time.sleep(1)
pyautogui.press('enter')  # Press Enter to navigate to the website
time.sleep(3)  # Wait for the website to load
print("copy all the data from website")
pyautogui.hotkey('ctrl','a',interval=0.1)  # Select all content on the page
time.sleep(1)   
pyautogui.hotkey('ctrl','c',interval=0.1)  # Copy the selected content
time.sleep(1)
print("open text editor and paste the data") 
pyautogui.hotkey('win','r',interval=0.1)  # Open the Run dialog
time.sleep(1)
pyautogui.write('notepad', interval=0.15)  # Type 'notepad' to open Notepad
time.sleep(1)
pyautogui.press('enter')  # Press Enter to open Notepad
time.sleep(3)  # Wait for Notepad to open
pyautogui.hotkey('ctrl','v',interval=0.1)  # Paste the copied content   

print("Save and close the notepad")
pyautogui.hotkey('ctrl','s',interval=0.1)  # Save the document
time.sleep(1)
pyautogui.hotkey('alt','f4',interval=0.1)  # Close the window
time.sleep(1)
