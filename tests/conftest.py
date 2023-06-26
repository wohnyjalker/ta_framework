import config
import pytest
from pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def log_in(request, driver):
    """
    This fixture will login user.
    Use @pytest.mark.no_login to prevent this behaviour
    """
    driver.delete_all_cookies()
    if request.node.get_closest_marker("no_login"):
        return
    login_page = LoginPage(driver).load_from_url(config.site_login_page)
    page = login_page.log_in(config.user_email, config.email_password)
    login_page.wait_for_page_to_load()
    return page
