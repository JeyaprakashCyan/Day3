import pyautogui
import pyperclip
import time
import os
import re
from datetime import datetime


# ============================================================
# DAILY WEATHER REPORT AUTOMATION BOT
# ============================================================
# Tools:
# PyAutoGUI
# Google Chrome
# Microsoft Excel
# ============================================================


# ============================================================
# STEP 1 - SETTINGS
# ============================================================

# Change the location here if required
LOCATION = "Bengaluru"

# Google Weather search URL
WEATHER_URL = f"https://www.google.com/search?q=weather+{LOCATION}"

# Create a folder on Desktop for reports
SAVE_FOLDER = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "DailyReports"
)

os.makedirs(SAVE_FOLDER, exist_ok=True)


# ============================================================
# STEP 2 - DATE AND FILE NAMES
# ============================================================

now = datetime.now()

DATE_TIME = now.strftime("%Y-%m-%d %H:%M:%S")
TODAY = now.strftime("%Y-%m-%d")

# Excel file name
EXCEL_FILE = os.path.join(
    SAVE_FOLDER,
    f"daily_report_{TODAY}.xlsx"
)

# Screenshot file name
SCREENSHOT_FILE = os.path.join(
    SAVE_FOLDER,
    f"daily_report_{TODAY}.png"
)


# ============================================================
# STEP 3 - PYAUTOGUI SETTINGS
# ============================================================

pyautogui.PAUSE = 1

# Move mouse to top-left corner to stop the program
# if something goes wrong.
pyautogui.FAILSAFE = True


# ============================================================
# STEP 4 - OPEN GOOGLE CHROME
# ============================================================

print("STEP 1: Opening Google Chrome...")

pyautogui.hotkey("win", "r")

time.sleep(1)

pyautogui.write(
    "chrome",
    interval=0.05
)

pyautogui.press("enter")

time.sleep(5)

print("Chrome opened successfully.")


# ============================================================
# STEP 5 - OPEN GOOGLE WEATHER
# ============================================================

print("STEP 2: Opening Google Weather...")

pyautogui.hotkey("ctrl", "l")

pyautogui.write(
    WEATHER_URL,
    interval=0.02
)

pyautogui.press("enter")

time.sleep(7)

print("Weather page opened.")


# ============================================================
# STEP 6 - COPY WEATHER INFORMATION
# ============================================================

print("STEP 3: Copying weather information...")

# Select visible page content
pyautogui.hotkey("ctrl", "a")

time.sleep(1)

# Copy
pyautogui.hotkey("ctrl", "c")

time.sleep(2)

# Get copied text
page_text = pyperclip.paste()

print("Weather information copied successfully.")


# ============================================================
# STEP 7 - GET LOCATION
# ============================================================

print("STEP 4: Getting location...")

# Location is entered through the browser search
weather_location = LOCATION

print("Location:", weather_location)


# ============================================================
# STEP 8 - FIND TEMPERATURE
# ============================================================

print("STEP 5: Finding temperature...")

temperature = None

# Search for Celsius or Fahrenheit values
temperature_patterns = [
    r"-?\d+\s*°C",
    r"-?\d+\s*°F",
    r"-?\d+\s*C",
    r"-?\d+\s*F"
]

for pattern in temperature_patterns:

    match = re.search(
        pattern,
        page_text
    )

    if match:
        temperature = match.group(0)
        break


# If temperature is not found
if temperature is None:

    temperature = "Temperature not detected"


print("Temperature:", temperature)


# ============================================================
# STEP 9 - CREATE COMMENT
# ============================================================

print("STEP 6: Creating comment...")

if "not detected" in temperature.lower():

    comment = (
        "Weather information could not be detected automatically."
    )

else:

    comment = "Good for outdoor activities."


print("Comment:", comment)


# ============================================================
# STEP 10 - OPEN MICROSOFT EXCEL
# ============================================================

print("STEP 7: Opening Microsoft Excel...")

pyautogui.hotkey("win", "r")

time.sleep(1)

pyautogui.write(
    "excel",
    interval=0.05
)

pyautogui.press("enter")

time.sleep(7)

print("Microsoft Excel opened.")


# ============================================================
# STEP 11 - CREATE NEW WORKBOOK
# ============================================================

print("STEP 8: Creating new Excel workbook...")

pyautogui.hotkey("ctrl", "n")

time.sleep(3)


# ============================================================
# STEP 12 - ENTER HEADER ROW
# ============================================================

print("STEP 9: Entering Excel headers...")

# A1
pyautogui.write(
    "Date & Time",
    interval=0.03
)

pyautogui.press("tab")


# B1
pyautogui.write(
    "Location",
    interval=0.03
)

pyautogui.press("tab")


# C1
pyautogui.write(
    "Temperature",
    interval=0.03
)

pyautogui.press("tab")


# D1
pyautogui.write(
    "Comment",
    interval=0.03
)

pyautogui.press("enter")


# ============================================================
# STEP 13 - ENTER WEATHER DATA
# ============================================================

print("STEP 10: Entering weather data...")

# A2 - Date & Time
pyautogui.write(
    DATE_TIME,
    interval=0.03
)

pyautogui.press("tab")


# B2 - Location
pyautogui.write(
    weather_location,
    interval=0.03
)

pyautogui.press("tab")


# C2 - Temperature
pyautogui.write(
    temperature,
    interval=0.03
)

pyautogui.press("tab")


# D2 - Comment
pyautogui.write(
    comment,
    interval=0.03
)

print("Weather report entered successfully.")


# ============================================================
# STEP 14 - FORMAT HEADER
# ============================================================

print("STEP 11: Formatting Excel header...")

# Go to A1
pyautogui.hotkey("ctrl", "home")

time.sleep(1)

# Select first row
pyautogui.hotkey("shift", "space")

time.sleep(1)

# Bold the header
pyautogui.hotkey("ctrl", "b")

time.sleep(1)


# ============================================================
# STEP 15 - AUTOFIT COLUMNS
# ============================================================

print("STEP 12: Adjusting column widths...")

# Go to A1
pyautogui.hotkey("ctrl", "home")

# Select used data
pyautogui.hotkey("ctrl", "a")

time.sleep(1)

# Excel Home menu
pyautogui.hotkey("alt", "h")

time.sleep(1)

# Format menu
pyautogui.press("o")

time.sleep(1)

# AutoFit Column Width
pyautogui.press("i")

time.sleep(2)

print("Column widths adjusted.")


# ============================================================
# STEP 16 - SAVE EXCEL FILE
# ============================================================

print("STEP 13: Saving Excel file...")

pyautogui.hotkey(
    "ctrl",
    "shift",
    "s"
)

time.sleep(4)


# Enter the complete file path
pyautogui.hotkey(
    "ctrl",
    "a"
)

pyautogui.write(
    EXCEL_FILE,
    interval=0.01
)

time.sleep(1)

pyautogui.press("enter")

time.sleep(5)


# ============================================================
# STEP 17 - HANDLE POSSIBLE EXCEL CONFIRMATION
# ============================================================

print("Checking for Excel confirmation...")

# Press Enter if a confirmation dialog appears
pyautogui.press("enter")

time.sleep(3)


# ============================================================
# STEP 18 - TAKE SCREENSHOT
# ============================================================

print("STEP 14: Taking screenshot of final Excel sheet...")

# Make sure Excel is active
pyautogui.click()

time.sleep(2)

# Take screenshot
screenshot = pyautogui.screenshot()

# Save screenshot
screenshot.save(
    SCREENSHOT_FILE
)

print("Screenshot saved successfully.")


# ============================================================
# STEP 19 - SAVE EXCEL AGAIN
# ============================================================

print("STEP 15: Saving Excel workbook again...")

pyautogui.hotkey(
    "ctrl",
    "s"
)

time.sleep(4)

print("Excel workbook saved successfully.")


# ============================================================
# STEP 20 - CLOSE EXCEL
# ============================================================

print("STEP 16: Closing Microsoft Excel...")

pyautogui.hotkey(
    "alt",
    "f4"
)

time.sleep(4)


# ============================================================
# STEP 21 - HANDLE POSSIBLE SAVE CONFIRMATION
# ============================================================

print("Checking for save confirmation...")

# If Excel asks to save changes,
# press Enter to confirm.
pyautogui.press("enter")

time.sleep(3)


# ============================================================
# STEP 22 - FINAL REPORT
# ============================================================

print()
print("=" * 65)
print("       DAILY WEATHER REPORT COMPLETED")
print("=" * 65)

print()
print("Date & Time :", DATE_TIME)
print("Location    :", weather_location)
print("Temperature :", temperature)
print("Comment     :", comment)

print()
print("Excel file saved at:")
print(EXCEL_FILE)

print()
print("Screenshot saved at:")
print(SCREENSHOT_FILE)

print()
print("Excel has been saved and closed successfully.")

print("=" * 65)