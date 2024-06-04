import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


class SeleniumUtils:
    def __init__(self, driver):
        self.driver = driver

    def video_ready(self):
        """
        Wait until the video is ready to play
        :return: bool
        """
        try:
            video_element = self.driver.find_element(By.TAG_NAME, "video")
            return video_element.get_attribute("readyState") == "4"
        except NoSuchElementException:
            return False

    def close_popups(self):
        """
        General method to close any pop-up
        :return: bool
        """
        # TODO - locators need to be modified when real pop up will be caught.
        try:
            popup_selectors = [
                (By.CLASS_NAME, "popup-class-name"),  # Replace with actual class name
                (By.ID, "popup-id"),  # Replace with actual ID
                (By.XPATH, "//button[text()='Close']"),  # Common close button
                (By.CSS_SELECTOR, ".popup-close-button")  # Replace with actual CSS selector
            ]

            for by, value in popup_selectors:
                elements = self.driver.find_elements(by, value)
                for element in elements:
                    if element.is_displayed():
                        element.click()
                        logger.info(f"Closed pop-up: {value}")
                        return True

        except Exception as e:
            logger.info(f"No pop-up found: {e}")
        return False

    def make_screenshot_by_name(self, screen_name):
        """
        Take a screenshot and save it with the given name
        :param screen_name: str
        :return: bool
        """
        if os.path.exists(screen_name):
            os.remove(screen_name)
            logger.info("Old screenshot deleted.")
        self.driver.save_screenshot(screen_name)
        return os.path.exists(screen_name)

    def get_scroll_position(self):
        return self.driver.execute_script("return window.pageYOffset;")

    def scroll_down(self, scroll_amount, step_size=500, wait_time=3):
        """
        Scroll down the page by a specific amount.

        :param scroll_amount: Total amount to scroll
        :param step_size: Amount to scroll in each step (default: 500 pixels)
        :param wait_time: Time to wait between scrolls (default: 2 seconds)
        :return: bool
        """
        initial_scroll_position = self.get_scroll_position()
        logger.debug(f"Initial scroll position: {initial_scroll_position}")

        for _ in range(scroll_amount):
            self.driver.execute_script(f"window.scrollBy(0, {step_size});")
            time.sleep(wait_time)
            current_scroll_position = self.get_scroll_position()
            logger.debug(f"Current scroll position: {current_scroll_position}")

        final_scroll_position = self.get_scroll_position()
        logger.debug(f"Final scroll position: {final_scroll_position}")

        return final_scroll_position > initial_scroll_position

    def is_element_in_viewport(self, element):
        """
        Check if an element is in the viewport
        :param element: WebElement
        :return: bool
        """
        return self.driver.execute_script(
            "var rect = arguments[0].getBoundingClientRect();"
            "return ("
            "rect.top >= 0 && "
            "rect.left >= 0 && "
            "rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && "
            "rect.right <= (window.innerWidth || document.documentElement.clientWidth)"
            ");",
            element
        )
