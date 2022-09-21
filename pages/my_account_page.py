from libs.base_page import BasePage
from libs.locator import Locator


class MyAccountPage(BasePage):
    logged_user = Locator(".account > span")

    def get_logged_user(self) -> str:
        return self.find_visible_element(self.logged_user).text
