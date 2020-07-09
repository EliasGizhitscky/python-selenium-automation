from behave import when, then
from selenium.webdriver.common.by import By



Cart_link = By.CSS_SELECTOR,'div#nav-tools a#nav-cart'
h_in_empty_cart = By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']"
cart_count = By.ID,("nav-cart-count")
Search_field = By.ID,('twotabsearchtextbox')
Submit_btn = By.CSS_SELECTOR, ("div.nav-search-submit input")
price_lnk = By.CSS_SELECTOR, ("span.a-price-whole")
add_cart_in_item_discr = By.ID, ('add-to-cart-button')


@when('Click on a cart icon')
def click_on_a_cart_link(context):
    context.app.main_page.click_on_cart()


@when('Search for {product} in search menu')
def search_from_homepage(context,product):
    context.app.main_page.search_for_keyword(product)


@when('Add the first result to cart')
def add_first_result(context):
    context.app.search_results_page.add_the_first_result()


@then('Verify that the cart is empty')
def verify_cart(context):
    context.app.cart_page.verify_the_cart_is_empty()


@then('Verify that the number of cart items is {items}')
def vrf_cart_count_is_1(context, items):
    context.app.cart_page.verify_number_of_cart_items(items)

