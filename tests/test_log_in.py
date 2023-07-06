import random
import string
import sys

import config
import pytest
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage

ERROR_MSG = (
    "The account sign-in was incorrect or your"
    " account is disabled temporarily."
    " Please wait and try again later."
)

personal_data = (
    f"{config.user_first_name} {config.user_last_name}\n{config.user_email}"
)
welcome_message = f"Welcome, {config.user_first_name} {config.user_last_name}!"


@pytest.mark.no_login
def test_login(driver):
    """Simple test to log in"""
    login_page = LoginPage(driver).load_from_url(config.site_login_page)
    my_account_page = login_page.log_in(
        config.user_email, config.email_password
    )
    my_account_page.wait_for_page_to_load()
    assert my_account_page.get_logged_user_personal_data() == personal_data


def test_login_personal_data_section(driver):
    """This test is using log_in auto-use fixture to remove redundant code"""
    my_account_page = MyAccountPage(driver)
    assert my_account_page.get_logged_user_personal_data() == personal_data


@pytest.mark.xfail(
    reason="TODO: add function/method to wait for top banner,"
    " watch out for StaleElementReference"
)
def test_login_top_message_bar(driver):
    my_account_page = MyAccountPage(driver)
    assert my_account_page.get_logged_user_top_msg() == welcome_message


@pytest.mark.no_login
def test_wrong_credentials(driver):
    login_page = LoginPage(driver).load_from_url(config.site_login_page)
    # added random email because when same email is used more than once
    # error related to captcha is shown
    email = f"{''.join(random.sample(string.ascii_lowercase, 10))}@email.com"
    login_page.fill_login_form(email, "wrong_password")
    login_page.get_submit_button().click()
    assert login_page.get_error_message() == ERROR_MSG


@pytest.mark.skip(reason="Test case not implemented")
def test_login_not_implemented_test_func():
    ...


def test_login_skipped_from_inside_of_test_func():
    if sys.platform == "darwin":
        pytest.skip(reason="Test cannot run on the MacOS system")
    assert True
