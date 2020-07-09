from selenium.webdriver.common.by import By
from behave import given, when, then



Search_field = By.ID,('twotabsearchtextbox')
Submit_btn = By.CSS_SELECTOR, ("div.nav-search-submit input")
RESULTS=By.CSS_SELECTOR,("a.a-link-normal span.a-size-base-plus")

@given('Open Amazon page')
def open_google(context):
    context.app.main_page.open_page()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    context.app.main_page.search_for_keyword(search_word)


@then('First result contains {search_word}')
def verify_first_result(context, search_word):
    context.app.search_results_page.verify_result_shown(search_word)
