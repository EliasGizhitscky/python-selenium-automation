from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_FIELD = By.ID, ('twotabsearchtextbox')
    SUBMIT_BTN = By.CSS_SELECTOR, ("div.nav-search-submit input")
    SELL_TOP_NAV_LNK = By.XPATH, "//div[@id='nav-xshop']/a[text()='Sell']"
    CART_LINK = By.CSS_SELECTOR, 'div#nav-tools a#nav-cart'
    NAV_LINKS = By.CSS_SELECTOR, ('div#nav-xshop a:not(.nav-hidden-aria  )')

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SUBMIT_BTN)

    def click_on_sell_button(self):
        self.click(*self.SELL_TOP_NAV_LNK)

    def click_on_cart(self):
        self.click(*self.CART_LINK)

    def top_nav_links_check(self):
        TODAYS_DEALS_CHECK = By.CSS_SELECTOR, ('h1 b')
        CUSTOMER_SERVICE_CHECK = By.CSS_SELECTOR, ('div.a-spacing-top-extra-large h1')
        GIFT_CARDDS_CHECK = By.CSS_SELECTOR, ('div#nav-subnav a.nav-b span')
        REGISTRY_CHECK = By.XPATH, ('//h3[text()[contains(.,"Registry discounts")]]')
        SELL_CHECK = By.CSS_SELECTOR, "div.align-center a"

        links_webelements = self.driver.find_elements(*self.NAV_LINKS)
        check_list = [TODAYS_DEALS_CHECK, CUSTOMER_SERVICE_CHECK, GIFT_CARDDS_CHECK, REGISTRY_CHECK, SELL_CHECK]
        asrt_list = ['Deals and Promotions', 'Hello. What can we help you with?', 'Gift Cards',
                     'Registry discounts, rewards and bonus gifts', 'Start selling']
        for x in range(len(links_webelements)):
            link = self.driver.find_elements(*self.NAV_LINKS)
            link[x].click()
            element_found = self.driver.find_element(*check_list[x])
            actual_rslt = element_found.text
            expected_rslt = asrt_list[x]
            assert actual_rslt == expected_rslt, f'Expected is {expected_rslt}, but got {asrt_list}'
