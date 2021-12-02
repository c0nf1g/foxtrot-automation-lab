from config import constants
from config.constants import XPATH_HEADER_H1
from locators.category_results import CategoryResultsLocators
from pages.base import Base


class CategoryResultsPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def open_item(self, item_name):
        item = self.find_element_by_text(item_name, tag=constants.XPATH_LINK_ELEMENTS)
        item.click()

    def is_category_name_valid(self, category):
        category_name = self.find_element_by_text(category, tag=XPATH_HEADER_H1)
        return category_name.text == category

    def is_results_relevant(self, item_category):
        items_headers = self._get_items_headers()
        return [True if (item_category in header) else False for header in items_headers]

    def _get_items_headers(self):
        items = self.find_elements(CategoryResultsLocators.LOCATOR_ITEM_HEADER)
        return [item.text for item in items]
