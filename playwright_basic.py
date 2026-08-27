from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/live-cricket-scores/")
    page.screenshot(path="cricbuzz.png")
    print(page.title())
    browser.close()