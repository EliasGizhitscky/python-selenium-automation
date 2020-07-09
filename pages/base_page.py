class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'

    def click (self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def open_page(self, url=''):
        self.driver.get(self.base_url+url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected text is {expected_text}, but got {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected {expected_url}, but got {actual_url}'