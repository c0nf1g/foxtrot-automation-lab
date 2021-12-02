from selenium.webdriver import ActionChains

from config import constants
from config.settings import Settings
from pages.base import Base


class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.set_page_load_timeout(20)
        self.driver.get(Settings.BASE_URL)

    def is_site_belongs_to_foxtrot(self):
        link = self.find_element_by_text(constants.COPYRIGHT)
        return link.text == constants.COPYRIGHT

    def open_section(self, section):
        section = self.find_element_by_text(section)
        self._move_mouse_over_element(section)

    def go_to_category(self, category):
        category = self.find_element_by_text(category, tag=constants.XPATH_LINK_ELEMENTS)
        category.click()

    def _move_mouse_over_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
