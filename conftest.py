import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    """TODO: add browser factory"""
    driver = Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()
