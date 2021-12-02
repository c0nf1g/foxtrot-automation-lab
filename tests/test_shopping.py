import pytest
from faker import Faker

from config import constants
from config.settings import Settings
from pages.category_results import CategoryResultsPage
from pages.checkout import CheckoutPage
from pages.home import HomePage
from pages.item_detail import ItemDetailPage
from tools.driver_singleton import DriverSingleton


@pytest.fixture(scope='session')
def browser(request):
    driver = DriverSingleton(request.param).get_driver()
    yield driver
    driver.close()


class TestShopping:
    @pytest.mark.parametrize("browser", ["chrome"], indirect=True)
    def test_buy_laptop(self, browser):
        home = HomePage(browser)

        assert home.is_site_belongs_to_foxtrot()

        home.open_section(constants.LAPTOPS_COMPUTERS_TABLETS_SECTION)
        home.go_to_category(constants.LAPTOPS_CATEGORY)

        category_results = CategoryResultsPage(browser)

        assert category_results.is_category_name_valid(constants.LAPTOPS_CATEGORY)
        assert category_results.is_results_relevant(constants.LAPTOP_CATEGORY)

        category_results.open_item(constants.LAPTOP_NAME)

        item_detail = ItemDetailPage(browser)

        assert item_detail.is_item_name_valid(constants.LAPTOP_NAME)
        item_price = item_detail.get_item_price()

        item_detail.buy_item()
        item_detail.go_to_checkout()

        checkout = CheckoutPage(browser)

        assert checkout.is_checkout_price_equal_to_detail(item_price)

        customer = Faker(Settings.FAKER_LOCALE)
        checkout.fill_contact_data(
            customer.phone_number(), customer.first_name(),
            customer.last_name(), customer.email()
        )
