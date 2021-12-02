from selenium import webdriver
from config.constants import CHROME_DRIVER, OPERA_DRIVER, SAFARI_DRIVER, EDGE_DRIVER, FIREFOX_DRIVER


class DriverFactory:
    @staticmethod
    def get_driver(driver_name=CHROME_DRIVER):
        if driver_name.lower() == CHROME_DRIVER:
            _single_web_driver = webdriver.Chrome()
        elif driver_name.lower() == FIREFOX_DRIVER:
            _single_web_driver = webdriver.Firefox()
        elif driver_name.lower() == EDGE_DRIVER:
            _single_web_driver = webdriver.Edge()
        elif driver_name.lower() == SAFARI_DRIVER:
            _single_web_driver = webdriver.Safari()
        elif driver_name.lower() == OPERA_DRIVER:
            _single_web_driver = webdriver.Opera()
        else:
            raise ValueError('Unknown name of browser')
        return _single_web_driver
