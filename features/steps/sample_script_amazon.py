from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(1)

@when('Click on start selling button')
def click_on_sell(context):
    context.driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[text()='Sell']").click()
    sleep(1)
    context.driver.find_element(By.XPATH, '//*[@id="eventColor"]/div[3]/div/div/div[1]/div/div[1]/div[3]/div/div/a').click()
    sleep(1)

@then('Verify Sign in page is opened')
def verify_signin_url(context):
    assert 'https://sellercentral.amazon.com/ap/signin' in context.driver.current_url
    sleep(1)
    context.driver.quit()