from pages.main_page import Page
from selenium.webdriver.common.by import By


class Cart(Page):
    CART_COUNT = By.ID, ('nav-cart-count')

    def verify_the_cart_is_empty(self):
        self.verify_text('0',*self.CART_COUNT)

    def verify_number_of_cart_items(self, expected_items):
        actual_items = self.driver.find_element(*self.CART_COUNT).text
        assert expected_items in actual_items, f'Expected {expected_items}, but got {actual_items}'
