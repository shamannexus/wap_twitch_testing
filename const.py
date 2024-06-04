from selenium.webdriver.common.by import By

class General:
    SITE_URL = "https://m.twitch.tv/"
    EMULATOR = "Nexus 5"
    SEARCH_TITLE = "StarCraft II"
    SEARCH_TITLE_URL = "directory/category/starcraft-ii"
    LOADING_TIMER = 5
    BLOCKED_SCREENSHOT_NAME = "blocked_screenshot.png"
    STREAM_SCREENSHOT_NAME = "stream_screenshot.png"

class Locators:
    POP_UP_BTH = (By.CLASS_NAME, "jmTjSc")
    # another variant, could be more stable, if classes are subject to often changes
    # POP_UP_BTH = (By.XPATH, "//button/div/div[contains(text(), 'Close')]")
    COOKIES_POP_UP = (By.CLASS_NAME, "eTsvyN")
    SEARCH_ICON = (By.CSS_SELECTOR, "a[href='/search']")
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    FIRST_RESULT = (By.XPATH, f"//p[@title='{General.SEARCH_TITLE}']")
    VIEWERS = (By.XPATH, "//div[contains(text(), 'viewers')]")