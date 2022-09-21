import pytest

import config
from libs.locator import Locator
from libs.base_page import BasePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage


@pytest.mark.no_login
def test_login(driver):
    page = BasePage(driver).load_from_url(config.site_url)
    page.find_clickable_element(Locator(".login")).click()
    page.find_visible_element(Locator("#email")).send_keys(config.user_email)
    page.find_visible_element(Locator("#passwd")).send_keys(config.email_password)
    page.find_clickable_element(Locator("#SubmitLogin")).click()
    assert page.find_visible_element(Locator(".account > span")).text == "* *"


@pytest.mark.no_login
def test_login_2(driver):
    login_page = LoginPage(driver).load_from_url(config.site_login_page)
    my_account_page = login_page.log_in(config.user_email, config.email_password)
    assert my_account_page.get_logged_user() == "* *"


def test_login_using_3(driver):
    """This test is using log_in autouse fixture"""
    my_account_page = MyAccountPage(driver)
    assert my_account_page.get_logged_user() == "* *"


@pytest.mark.no_login
def test_wrong_credentials(driver):
    login_page = LoginPage(driver).load_from_url(config.site_login_page)
    login_page.fill_login_form("wrong@user.com", "wrong_password")
    login_page.get_submit_button().click()
    assert login_page.get_error_message() == "Authentication failed."
