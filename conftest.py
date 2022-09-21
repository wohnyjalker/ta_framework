import pytest
from selenium.webdriver import Chrome, Remote
from webdriver_manager.chrome import ChromeDriverManager

import config


@pytest.fixture(scope="session")
def driver():
    """TODO: add browser factory"""
    if config.is_remote:
        driver = Remote(command_executor=config.remote_address)
    else:
        driver = Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()
