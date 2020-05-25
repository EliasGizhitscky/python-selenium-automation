from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

Cart_link = By.CSS_SELECTOR,'div#nav-tools a#nav-cart'
h_in_empty_cart = By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']"
cart_count = By.ID,('nav-cart-count')
Search_field = By.ID,('twotabsearchtextbox')
Submit_btn = By.CSS_SELECTOR, ("div.nav-search-submit input")
price_lnk = By.CSS_SELECTOR, ("span.a-price-whole")
add_cart_in_item_discr = By.ID, ('add-to-cart-button')


@when('Click on a cart icon')
def click_on_a_cart_link(context):
    context.driver.find_element(*Cart_link).click()
    sleep(1)

@when('Searh for Wi-Fi router in searh menu')
def search_from_homepage(context):
    context.driver.find_element(*Search_field).send_keys('router')
    context.driver.find_element(*Submit_btn).click()


@when('Add the first result to cart')
def add_frst_rslt(context):
    context.driver.find_element(*price_lnk).click()
    context.driver.find_element(*add_cart_in_item_discr).click()


@then('Verify that the cart is empty')
def verify_cart_is_empty(context):
    actual_items = context.driver.find_element(*cart_count).text
    assert '0' in actual_items
    print('Expected result is "0" and the actual result is "{}"'.format(actual_items))
    context.driver.quit()

@then('Verify that the number of cart items is 1')
def vrf_cart_count_is_1(context):
    actual_items = context.driver.find_element(*cart_count).text
    assert '1' in actual_items
    print('Expected result is "1" and the actual result is "{}"'.format(actual_items))
    context.driver.quit()
