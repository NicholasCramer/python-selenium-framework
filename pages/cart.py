from selenium.webdriver.common.by import By

from pages.confirm import ConfirmPage


class CartPage:

    def __init__(self, browser):
        self.browser = browser

    checkout_btn = (By.CSS_SELECTOR, ".btn.btn-success")

    def go_to_checkout(self):
        self.browser.find_element(*CartPage.checkout_btn).click()
        confirm_page = ConfirmPage(self.browser)
        return confirm_page

