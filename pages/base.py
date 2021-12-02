from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import constants
from locators.default import DefaultLocators
from tools.driver_factory import DriverFactory


class Base:
    def __init__(self, driver):
        self.driver = driver if driver else DriverFactory.get_driver()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(locator)
        )

    def find_element_by_text(self, text, tag=constants.XPATH_ALL_ELEMENTS):
        locator = self._get_locator_with_custom_x_path(text, tag)
        return self.find_element(locator)

    def fill_data(self, data, locator):
        field = self.find_element(locator)
        field.click()
        field.send_keys(data)
        return field

    @staticmethod
    def _get_locator_with_custom_x_path(text, tag):
        locator = list(DefaultLocators.LOCATOR_ELEMENT_CONTAINS_TEXT)
        locator[1] = DefaultLocators.LOCATOR_ELEMENT_CONTAINS_TEXT[1].format(tag, text)
        return tuple(locator)
