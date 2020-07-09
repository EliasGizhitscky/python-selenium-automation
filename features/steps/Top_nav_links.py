from behave import then


@then('Verify that every link in top nav menu leads to appropriate page')
def lnks_check(context):
    context.app.main_page.top_nav_links_check()




