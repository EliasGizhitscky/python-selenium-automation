from pages.base_page import Page

class LogIn(Page):
    loginUrl = 'https://sellercentral.amazon.com/ap/signin'

    def login_page_opn(self):
        self.verify_url(self.loginUrl)

