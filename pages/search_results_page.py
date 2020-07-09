from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):

    RESULTS = By.CSS_SELECTOR, ("a.a-link-normal span.a-size-base-plus")
    PRICE_LINK = By.CSS_SELECTOR, ("span.a-price-whole")
    ADD_TO_CART_IN_ITEM_DISCR = By.ID, ('add-to-cart-button')
    COLOR_OPTION = By.CSS_SELECTOR,('div#variation_color_name li')
    SELECTED_COLOR = By.CSS_SELECTOR,('div#variation_color_name span.selection')

    def verify_result_shown(self, expected_text):
        self.verify_text(expected_text, *self.RESULTS)

    def add_the_first_result(self):
        self.driver.find_element(*self.PRICE_LINK).click()
        self.driver.find_element(*self.ADD_TO_CART_IN_ITEM_DISCR).click()

    def open_product_page(self):
        self.open_page('/dp/B07RL5Z29Z')

    def check_for_color_selection(self):
        expected_colors = ['New Dark Wash', 'New Medium Wash', 'Rinse', 'Dark Wash', 'Medium Wash']
        color_webelements = self.driver.find_elements(*self.COLOR_OPTION)
        for x in range(len(color_webelements)):
            color_webelements[x].click()

            actual_color = self.driver.find_element(*self.SELECTED_COLOR).text
            assert actual_color == expected_colors[x], f'Expected color is {expected_colors[x]}, but got {actual_color}'

            print('Colors changing are working correctly')