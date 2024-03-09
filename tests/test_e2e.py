import pytest
from pages.cart import CartPage
from pages.confirm import ConfirmPage
from pages.shop import ShopPage
from pages.home import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class TestOne(BaseClass):

    def test_e2e(self):

        home_page = HomePage(self.browser)
        home_page.get_shop_items().click()
        shop_page = ShopPage(self.browser)
        product_elements = shop_page.get_product_elements()
        for product in product_elements:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        shop_page.get_cart_button().click()
        cart_page = CartPage(self.browser)
        cart_page.get_checkout_button().click()
        confirm_page = ConfirmPage(self.browser)
        confirm_page.get_location_field().send_keys("United")
        confirm_page.get_search_suggestion().click()
        confirm_page.get_confirm_box().click()
        confirm_page.get_checkout_btn().click()

        success_text = confirm_page.get_success_text().text

        assert "Success! Thank you!" in success_text
