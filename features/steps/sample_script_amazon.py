from behave import when,then


@when('Click on Sell button')
def click_on_sell_btn(context):
    context.app.main_page.click_on_sell_button()


@when('Click on Sign Up button')
def click_on_signup_btn(context):
    context.app.sellers_page.click_on_sign_up_btn()


@then('Verify Sign in page is opened')
def sign_in_page_is_opened(context):
    context.app.log_in_page.login_page_opn()