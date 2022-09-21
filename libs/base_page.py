from typing import Optional

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from config import global_timeout
from libs.locator import Locator


class BasePage:
    def __init__(self, driver, timeout: float = global_timeout):
        self.driver = driver
        self.timeout = timeout

    def load_from_url(self, url: str):
        self.driver.get(url)
        return self

    def find_clickable_element(self, locator: Locator, timeout: Optional[float] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            ec.element_to_be_clickable((locator.method, locator.location))
        )

    def find_visible_element(self, locator: Locator, timeout: Optional[float] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            ec.visibility_of_element_located((locator.method, locator.location))
        )

    def find_all_present_elements(self, locator: Locator, timeout: Optional[float] = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            ec.presence_of_all_elements_located((locator.method, locator.location))
        )
