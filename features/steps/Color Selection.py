from behave import given, then
from selenium.webdriver.common.by import By
from time import sleep

Color_option = By.CSS_SELECTOR,('div#variation_color_name li')
Selected_color = By.CSS_SELECTOR,('div#variation_color_name span.selection')


@given ('Open product {productid} page')
def product_page_opn(context, productid):
    context.driver.get('https://www.amazon.com/dp/B07RL5Z29Z')


@then('Check for color selection of product')
def color_selection(context):
    expected_colors = ['New Dark Wash', 'New Medium Wash', 'Rinse', 'Dark Wash', 'Medium Wash']
    color_webelements = context.driver.find_elements(*Color_option)


    for x in range(len(color_webelements)):
        color_webelements[x].click()
        sleep(1)
        actual_color = context.driver.find_element(*Selected_color).text
        assert actual_color == expected_colors[x], f'Expected color is {expected_colors[x]}, but got {actual_color}'

    print('Colors changing are working correctly')

