import config
import pytest
from libs.allure_functions import attache_screenshot
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    print(item)


@pytest.fixture(autouse=True)
def attache_screenshot_on_fail(request, driver):
    yield  # use in the end of test function
    node = request.node
    if not node.rep_setup.passed:
        attache_screenshot(driver, node.name)
    if not node.rep_call.passed:
        attache_screenshot(driver, node.name)
