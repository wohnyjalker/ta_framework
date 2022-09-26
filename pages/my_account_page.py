from libs.base_page import BasePage
from libs.locator import Locator


class MyAccountPage(BasePage):
    logged_user = Locator(".account > span")
    sign_out = Locator(".logout")

    def get_logged_user(self) -> str:
        return self.find_visible_element(self.logged_user).text

    def get_sign_out_button(self):
        return self.find_clickable_element(self.sign_out)
