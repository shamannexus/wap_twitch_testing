import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from const import General

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    mobile_emulation = {"deviceName": General.EMULATOR}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Use ChromeDriverManager to manage the ChromeDriver installation
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    # common waiter for all steps
    driver.implicitly_wait(General.LOADING_TIMER)
    yield driver
    driver.quit()
