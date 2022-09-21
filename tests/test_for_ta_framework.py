import config
from libs.locator import Locator
from libs.base_page import BasePage
from pages.login_page import LoginPage


def test_login(driver):
    page = BasePage(driver).load_from_url(config.site_url)
    page.find_clickable_element(Locator(".login")).click()
    page.find_visible_element(Locator("#email")).send_keys(config.user_email)
    page.find_visible_element(Locator("#passwd")).send_keys(config.email_password)
    page.find_clickable_element(Locator("#SubmitLogin")).click()
    assert page.find_visible_element(Locator(".account > span")).text == "* *"


def test_login_2(driver):
    login_page = LoginPage(driver).load_from_url(
        "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    )
    my_account_page = login_page.log_in(config.user_email, config.email_password)
    assert my_account_page.get_logged_user() == "* *"
