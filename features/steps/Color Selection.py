from behave import given, then


@given('Open product page')
def product_page_opn(context):
    context.app.search_results_page.open_product_page()


@then('Check for color selection of product')
def color_selection(context):
    context.app.search_results_page.check_for_color_selection()

