from behave import given, then
from selenium.webdriver.common.by import By

PRODUCT_PRICE = By.CSS_SELECTOR,('from selenium.webdriver.common.by import By')
PRODUCT_NAME = By.CSS_SELECTOR,('span.wfm-sales-item-card__product-name')


@given('Open Amazon Wholefoodsdeals page')
def wholefood_page_opn(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify that every product has name and regular price')
def name_and_price_check(context):
    product_price_webelements = context.driver.find_elements(*PRODUCT_PRICE)
    for price in product_price_webelements:
        assert 'Regular' in price.text , f'Expected "Regular", but got {price}'

    product_name_webelements = context.driver.find_elements(*PRODUCT_NAME)
    for name in product_name_webelements:
        assert '' != name
