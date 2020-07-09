from pages.base_page import Page
from selenium.webdriver.common.by import By

class Wholefoodsdeals(Page):
    PRODUCT_PRICE = By.CSS_SELECTOR, ('div.a-row span.wfm-sales-item-card__regular-price')
    PRODUCT_NAME = By.CSS_SELECTOR, ('span.wfm-sales-item-card__product-name')

    def open_wholefoodsdeals_page(self):
        self.open_page('/wholefoodsdeals')

    def name_and_regular_price_check(self):
        product_price_webelements = self.driver.find_elements(*self.PRODUCT_PRICE)
        for price in product_price_webelements:
            assert 'Regular' in price.text, f'Expected "Regular", but got {price}'

        product_name_webelements = self.driver.find_elements(*self.PRODUCT_NAME)
        for name in product_name_webelements:
            assert '' != name.text


