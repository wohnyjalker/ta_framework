from libs.base_page import BasePage
from libs.locator import Locator
from selenium.webdriver.remote.webelement import WebElement


class MyAccountPage(BasePage):
    actions_menu = Locator("[data-action='customer-menu-toggle']")
    logged_user = Locator(".logged-in")
    sign_out = Locator(".authorization-link")
    first_last_name_box = Locator(".box-content > p:first-of-type")

    def get_actions_menu(self) -> WebElement:
        return self.find_visible_element(self.actions_menu)

    def get_logged_user_top_msg(self) -> str:
        return self.find_visible_element(self.logged_user).text

    def get_logged_user_personal_data(self) -> str:
        return self.find_visible_element(self.first_last_name_box).text

    def get_sign_out_button(self) -> WebElement:
        self.get_actions_menu().click()
        return self.find_clickable_element(self.sign_out)
