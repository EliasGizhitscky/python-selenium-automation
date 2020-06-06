from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

Products_price = By.CSS_SELECTOR,("li.s-result-item")
Products_name = By.CSS_SELECTOR, ("span.wfm-sales-item-card__product-name")

@given('Open Amazon Wholefoodsdeals page')
def wholefoodsdeals_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals ')
    sleep(2)

@then('Each product has a regular price and name')
def regular_price_and_name(context):
    products_webelements = context.driver.find_elements(*Products_price)
    for product_element in products_webelements:
        assert 'Regular' or 'Look for the blue signs in store.' in product_element.text, f'Expected "Regular" to be in {product_element.text}'

    product_names = context.driver.find_elements(*Products_name)
    for name in product_names:
        assert '' != name