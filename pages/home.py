from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def get_shop_items(self):
        return self.browser.find_element(*HomePage.shop)
