
import logging
import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from const import General, Locators
from utils import SeleniumUtils

logger = logging.getLogger(__name__)


class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.utils = SeleniumUtils(driver)

    def _step1_open_main_page(self):
        self.driver.get(General.SITE_URL)
        try:
            if pop_up_dialog_button := self.driver.find_element(*Locators.POP_UP_BTH):
                pop_up_dialog_button.click()
                assert "Twitch" in self.driver.title, f"Site {General.SITE_URL} was not loaded"
                return True
        except NoSuchElementException:
            logger.exception("Element not found, proceeding without performing actions")

        try:
            if self.driver.find_element(*Locators.COOKIES_POP_UP):
                self.utils.make_screenshot_by_name(General.BLOCKED_SCREENSHOT_NAME)
                pytest.skip("There is a bug that Cookies pop up are not closed when appear, "
                            "so in a case when this pop up appear - test skipped")
        except NoSuchElementException:
            pass

    def _step2_click_on_search_icon(self):
        if search_link := self.driver.find_element(*Locators.SEARCH_ICON):
            search_link.click()
        assert "search" in self.driver.current_url, "Search field is not opened"

    def _step3_input_testing_data(self):
        search_input = self.driver.find_element(*Locators.SEARCH_INPUT)
        search_input.send_keys(General.SEARCH_TITLE)
        assert search_input.get_attribute("value") != "", f"{General.SEARCH_TITLE} text was not inputted"

    def _step4_click_on_first_search_result(self):
        # TODO added here time sleep to be sure that as search_result value if 1 search results.
        #  Without this time sleep it will be just submitted search input field -
        #  and then search result will not be fully
        #  correct. it may be a bug with search. Need to be discussed.
        time.sleep(1)
        search_result = self.driver.find_element(*Locators.FIRST_RESULT)
        search_result.click()
        assert General.SEARCH_TITLE_URL in self.driver.current_url

    def _step5_scroll_down(self):
        time.sleep(4)
        assert self.utils.scroll_down(2), "Scrolls were not performed successfully."

    def _step6_open_streamer_page(self):
        try:
            streamers = self.driver.find_elements(*Locators.VIEWERS)
            for streamer in streamers:
                if self.utils.is_element_in_viewport(streamer):
                    logger.debug("Element is visible and performing actions.")
                    logger.debug(streamer.text)
                    coordinates = self.driver.execute_script("return arguments[0].getBoundingClientRect();", streamer)
                    offset_x = coordinates['left'] + coordinates['width'] / 2
                    offset_y = coordinates['top'] + coordinates['height'] / 2
                    actions = ActionChains(self.driver)
                    actions.move_by_offset(offset_x, offset_y).click().perform()
                    break
            else:
                logger.info("No visible element found.")
        except NoSuchElementException:
            logger.info("Element not found.")

    def _step7_wait_till_page_loaded_and_take_screenshot(self):
        self.utils.close_popups()
        wait = WebDriverWait(self.driver, 10)
        video_element = wait.until(lambda driver: self.utils.video_ready())
        assert video_element, "Video is not ready to play"
        assert self.utils.make_screenshot_by_name(General.STREAM_SCREENSHOT_NAME), "Failed to create new screenshot."

    def test_open_random_stream(self):
        self._step1_open_main_page()
        self._step2_click_on_search_icon()
        self._step3_input_testing_data()
        self._step4_click_on_first_search_result()
        self._step5_scroll_down()
        self._step6_open_streamer_page()
        self._step7_wait_till_page_loaded_and_take_screenshot()
