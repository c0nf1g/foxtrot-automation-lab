from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    LOCATOR_INPUT_TELEPHONE = (By.ID, 'Phone')
    LOCATOR_INPUT_NAME = (By.ID, 'Name')
    LOCATOR_INPUT_SURNAME = (By.ID, 'LastName')
    LOCATOR_INPUT_EMAIL = (By.ID, 'Email')
    LOCATOR_FINAL_PRICE = (By.CLASS_NAME, 'final-price')
