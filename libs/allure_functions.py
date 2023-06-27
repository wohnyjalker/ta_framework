import allure
from allure_commons.types import AttachmentType


def attache_screenshot(driver, name: str) -> None:
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=AttachmentType.PNG,
    )
