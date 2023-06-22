from libs.base_page import BasePage
from libs.locator import Locator
from pages.my_account_page import MyAccountPage
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):
    sign_in = Locator(".login")
    email_input = Locator("#email")
    password_input = Locator("#passwd")
    submit_btn = Locator("#SubmitLogin")
    error_message = Locator(".alert > ol > li")

    def fill_login_form(self, email: str, password: str):
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
