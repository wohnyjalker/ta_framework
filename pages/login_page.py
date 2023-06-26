from libs.base_page import BasePage
from libs.locator import Locator
from pages.my_account_page import MyAccountPage
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):
    sign_in = Locator(".authorization-link")
    email_input = Locator("#email")
    password_input = Locator("#pass")
    submit_btn = Locator("#send2")
    error_message = Locator(".message-error > div")

    def fill_login_form(self, email: str, password: str) -> None:
        self.find_visible_element(self.email_input).send_keys(email)
        self.find_visible_element(self.password_input).send_keys(password)

    def log_in(self, email: str, password: str) -> MyAccountPage:
        self.fill_login_form(email, password)
        self.find_clickable_element(self.submit_btn).click()
        return MyAccountPage(self.driver)

    def get_error_message(self) -> str:
        return self.find_visible_element(self.error_message).text

    def get_submit_button(self) -> WebElement:
        return self.find_clickable_element(self.submit_btn)
