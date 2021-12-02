from selenium.webdriver.common.by import By
from locators.default import DefaultLocators


class CategoryResultsLocators(DefaultLocators):
    LOCATOR_ITEM_HEADER = (By.CLASS_NAME, 'card__title')
