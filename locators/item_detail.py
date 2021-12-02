from selenium.webdriver.common.by import By
from locators.default import DefaultLocators


class ItemDetailLocators(DefaultLocators):
    LOCATOR_BASKET_BUTTON = (By.CLASS_NAME, "header-basket")
    LOCATOR_BUY_BUTTON = (By.CLASS_NAME, "product-box__main-buy__button")
    LOCATOR_ITEM_NAME = (By.CLASS_NAME, 'page__title')
    LOCATOR_CARD_PRICE = (By.CLASS_NAME, 'product-box__main-price__main_promo')
