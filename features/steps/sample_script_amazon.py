from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

sell_icon = By.XPATH,"//div[@id='nav-xshop']/a[text()='Sell']"
start_selling_button = By.XPATH,"//div[@class='align-center']/a"



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)


@when('Click on start selling button')
def click_on_sell(context):
    context.driver.find_element(*sell_icon).click()
    sleep(1)
    context.driver.find_element(*start_selling_button).click()
    sleep(1)


@then('Verify Sign in page is opened')
def verify_signin_url(context):
    assert 'https://sellercentral.amazon.com/ap/signin' in context.driver.current_url
    sleep(1)
    context.driver.quit()