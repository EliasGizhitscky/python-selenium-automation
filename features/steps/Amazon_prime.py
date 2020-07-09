from behave import given, when, then


@given('Open Amazon Prime page')
def amazon_prime_opn(context):
    context.app.prime_page.open_amazon_prime_page()


@then('Verify that is {numbers} boxes')
def cout_boxes(context, numbers):
    numbers = int(numbers)
    context.app.prime_page.verify_number_of_box_links(numbers)