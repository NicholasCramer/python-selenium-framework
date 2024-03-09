from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, browser):
        self.browser = browser

    checkout_btn = (By.CSS_SELECTOR, ".btn.btn-success")

    def get_checkout_button(self):
        return self.browser.find_element(*CartPage.checkout_btn)
