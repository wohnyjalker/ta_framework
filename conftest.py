import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    driver = Chrome(ChromeDriverManager().install())
    yield driver
    driver.close()
