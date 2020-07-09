from pages.base_page import Page
from selenium.webdriver.common.by import By


class Prime(Page):

    PRIME_BOXES = By.CSS_SELECTOR, ("div.benefit-box-text")
    def open_amazon_prime_page(self):
        self.open_page('/amazonprime')

    def verify_number_of_box_links(self,numbers_of_links):
        count_boxes = len(self.driver.find_elements(*self.PRIME_BOXES))
        assert count_boxes == numbers_of_links,f'Expected result is "8" and the actual result is "{count_boxes}"'
