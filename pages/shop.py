from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, browser):
        self.browser = browser

    product_elements = (By.XPATH, "//div[@class='card h-100']")
    cart_btn = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")

    def get_product_elements(self):
        return self.browser.find_elements(*ShopPage.product_elements)

    def get_cart_button(self):
        return self.browser.find_element(*ShopPage.cart_btn)
