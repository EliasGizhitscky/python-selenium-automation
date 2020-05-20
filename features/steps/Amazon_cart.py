from behave import when, then
from selenium.webdriver.common.by import By
from time import sleep

Cart_link = By.CSS_SELECTOR,'div#nav-tools a#nav-cart'
h_in_empty_cart = By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']"
cart_count = By.ID,('nav-cart-count')


@when('Click on a cart icon')
def click_on_a_cart_link(context):
    context.driver.find_element(*Cart_link).click()
    sleep(1)

@then('Verify that the cart is empty')
def verify_cart_is_empty(context):
    actual_items = context.driver.find_element(*cart_count).text
    assert '0' in actual_items
    print('Expected result is "0" and the actual result is "{}"'.format(actual_items))
    context.driver.quit()

