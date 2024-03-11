from selenium.webdriver.common.by import By

from pages.shop import ShopPage


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def navigate_to_shop(self):
        self.browser.find_element(*HomePage.shop).click()
        shop_page = ShopPage(self.browser)
        return shop_page
