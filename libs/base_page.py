import time
from typing import Any, Optional

from config import global_timeout
from libs.exceptions import PageLoadTimeoutException
from libs.locator import Locator
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    TODO: try different approach:
     1. create page elements (button, dropdown, input, etc)
     2. add base functionalities to elements
     3. create reusable components that consist of page elements
     4. add components to appropriate page
    """

    def __init__(self, driver, timeout: float = global_timeout):
        self.driver = driver
        self.timeout = timeout

    def load_from_url(self, url: str):
        self.driver.get(url)
        return self

    def find_clickable_element(
        self, locator: Locator, timeout: Optional[float] = None
    ):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            ec.element_to_be_clickable((locator.method, locator.location))
        )

    def find_visible_element(
        self, locator: Locator, timeout: Optional[float] = None
    ):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            ec.visibility_of_element_located(
                (locator.method, locator.location)
            )
        )

    def find_all_present_elements(
        self, locator: Locator, timeout: Optional[float] = None
    ):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            ec.presence_of_all_elements_located(
                (locator.method, locator.location)
            )
        )

    def execute_java_script(self, js_statement: str) -> Any:
        """
        TODO: maybe move to different file to not mess up
         with page -> js_browser_scripts?
        """
        return self.driver.execute_script(js_statement)

    def wait_for_page_to_load(self, timeout: int = 5):
        """TODO: maybe move to different file -> js_browser_scripts?"""
        started_at = time.time()
        while time.time() - started_at < timeout:
            if (
                self.execute_java_script("return document.readyState")
                == "complete"
            ):
                return
        raise PageLoadTimeoutException(f"Page load timeout {timeout} exceeded")
