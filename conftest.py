import config
import pytest
from selenium.webdriver import Chrome, ChromeOptions, Remote
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    """TODO: add browser factory"""
    if config.is_remote:
        chrome_options = ChromeOptions()
        driver = Remote(
            command_executor=config.remote_address, options=chrome_options
        )
    else:
        driver = Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()
