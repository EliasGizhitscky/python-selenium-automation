from behave import given, when, then
from selenium.webdriver.common.by import By



WHEATHER_LNK = By.CSS_SELECTOR, ('div.weather a.home-link_blue_yes')



@given ('Open yandex homepage')
def yandex_hp_opn(context):
    context.driver.get("https://yandex.ru/")

@when ('Store original window')
def store_original_window(context):
    original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles
    print('\nOriginal window\n', original_window)
    print('\nOld windows\n', context.old_windows)

@when('Click on weather link')
def cick_on_weather_lnk(context):
    context.driver.find_element(*WHEATHER_LNK).click()

@when('Switch to the  newly opened window')
def switch_to_new_window(context):

    current_windows = context.driver.window_handles
    print('\nCurrent_windows\n', current_windows)
    #new_window = current_windows[1]
    #context.driver.switch_to_window(new_window)
    new_window = current_windows
    for old_window in context.old_windows:
        new_window.remove(old_window)

    context.driver.switch_to_window(new_window[0])



@then ('Weather is shown')
def weather_is_shown(context):
    actual_url = context.driver.current_url
    assert 'https://yandex.ru/pogoda/' in actual_url, f'{actual_url}'
