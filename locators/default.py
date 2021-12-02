from selenium.webdriver.common.by import By


class DefaultLocators:
    LOCATOR_ELEMENT_CONTAINS_TEXT = (By.XPATH, "//{}[contains(text(), '{}')]")