from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

prime_boxes = By.CSS_SELECTOR, ("div.benefit-box-text")



@given('Open Amazon Prime page')
def amazon_prime_opn(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify that is 8 boxes')
def cout_boxes(context):
    count_boxes = int(len(context.driver.find_elements(*prime_boxes)))
    assert count_boxes == 8
    print('Expected result is "8" and the actual result is "{}"'.format(count_boxes))