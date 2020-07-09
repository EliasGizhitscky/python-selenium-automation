from behave import given, then

@given('Open Amazon Wholefoodsdeals page')
def wholefood_page_opn(context):
    context.app.wholefoodsdeals_page.open_wholefoodsdeals_page()


@then('Verify that every product has name and regular price')
def name_and_price_check(context):
    context.app.wholefoodsdeals_page.name_and_regular_price_check()
