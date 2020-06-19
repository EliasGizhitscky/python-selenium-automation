from behave import then
from selenium.webdriver.common.by import By
from time import sleep

NAV_LINKS = By.CSS_SELECTOR, ('div#nav-xshop a:not(.nav-hidden-aria  )')
TODAYS_DEALS = By.CSS_SELECTOR, ('h1 b')
CUSTOMER_SERVICE = By.CSS_SELECTOR, ('div.a-spacing-top-extra-large h1')
GIFT_CARDDS = By.CSS_SELECTOR, ('div#nav-subnav a.nav-b span')
REGISTRY = By.XPATH, ('//h3[text()[contains(.,"Registry discounts")]]')
SELL = By.XPATH,"//div[@class='align-center']/a"


@then('Verify that every link in top nav menu leads to appropriate page')
def lnks_check(context):
    links_webelements = context.driver.find_elements(*NAV_LINKS)
    check_list = [TODAYS_DEALS, CUSTOMER_SERVICE,GIFT_CARDDS,REGISTRY,SELL]
    asrt_list = ['Deals and Promotions', 'Hello. What can we help you with?','Gift Cards','Registry discounts, rewards and bonus gifts','Start selling']
    for x in range(len(links_webelements)):
        link = context.driver.find_elements(*NAV_LINKS)
        link[x].click()
        sleep(1)
        element_found = context.driver.find_element(*check_list[x])
        actual_rslt = element_found.text
        expected_rslt = asrt_list[x]
        assert actual_rslt == expected_rslt, f'Expected is {expected_rslt}, but got {asrt_list}'



