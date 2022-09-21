from libs.base_page import BasePage
from libs.locator import Locator
from pages.my_account_page import MyAccountPage


class LoginPage(BasePage):
    sign_in = Locator(".login")
    email_input = Locator("#email")
    password_input = Locator("#passwd")
    submit_btn = Locator("#SubmitLogin")

    def fill_login_form(self, email: str, password: str):
        self.find_visible_element(self.email_input).send_keys(email)
        self.find_visible_element(self.password_input).send_keys(password)

    def log_in(self, email: str, password: str) -> MyAccountPage:
        self.fill_login_form(email, password)
        self.find_clickable_element(self.submit_btn).click()
        return MyAccountPage(self.driver)
