from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.sellers_page import SellersPage
from pages.log_in_page import LogIn
from pages.cart_page import Cart
from pages.prime_page import Prime
from pages.wholefoodsdeals_page import Wholefoodsdeals


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.sellers_page = SellersPage(self.driver)
        self.log_in_page = LogIn(self.driver)
        self.cart_page = Cart(self.driver)
        self.prime_page = Prime(self.driver)
        self.wholefoodsdeals_page = Wholefoodsdeals(self.driver)
