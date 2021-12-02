from locators.checkout import CheckoutPageLocators
from pages.base import Base


class CheckoutPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_contact_data(self, telephone, name, surname, email):
        self._fill_telephone(telephone)
        self._fill_name(name)
        self._fill_surname(surname)
        self._fill_email(email)

    def _fill_telephone(self, telephone):
        return self.fill_data(telephone, CheckoutPageLocators.LOCATOR_INPUT_TELEPHONE)

    def _fill_name(self, name):
        return self.fill_data(name, CheckoutPageLocators.LOCATOR_INPUT_NAME)

    def _fill_surname(self, surname):
        return self.fill_data(surname, CheckoutPageLocators.LOCATOR_INPUT_SURNAME)

    def _fill_email(self, email):
        return self.fill_data(email, CheckoutPageLocators.LOCATOR_INPUT_EMAIL)

    def is_checkout_price_equal_to_detail(self, detail_price):
        checkout_price = self.find_element(CheckoutPageLocators.LOCATOR_FINAL_PRICE)
        final_price = int(checkout_price.text.replace('разом\n', '').replace('₴', '').replace(' ', ''))
        return final_price == detail_price
