from config import constants
from locators.item_detail import ItemDetailLocators
from pages.base import Base


class ItemDetailPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def buy_item(self):
        buy_button = self.find_element(ItemDetailLocators.LOCATOR_BUY_BUTTON)
        buy_button.click()

    def go_to_checkout(self):
        register_order_button = self.find_element_by_text(constants.REGISTER_ORDER_BUTTON_NAME,
                                                          tag=constants.XPATH_LINK_ELEMENTS)
        register_order_button.click()

    def is_item_name_valid(self, item_name):
        item_header = self.find_element(ItemDetailLocators.LOCATOR_ITEM_NAME)
        return item_header.text == item_name

    def get_item_price(self):
        card_price = self.find_element(ItemDetailLocators.LOCATOR_CARD_PRICE)
        price = int(card_price.text.replace('₴', '').replace(' ', ''))
        return price
