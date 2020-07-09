from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SellersPage (Page):

    SIGN_UP_BTN = By.XPATH, "//div[@class='align-center']/a[text()='Start selling']"

    def click_on_sign_up_btn(self):
        self.click(*self.SIGN_UP_BTN)

