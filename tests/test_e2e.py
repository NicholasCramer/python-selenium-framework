from pages.home import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class TestCheckoutProcess(BaseClass):

    def test_e2e(self):

        home_page = HomePage(self.browser)
        shop_page = home_page.navigate_to_shop()
        product_elements = shop_page.get_product_elements()
        for product in product_elements:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        cart_page = shop_page.get_cart_button()
        confirm_page = cart_page.go_to_checkout()
        confirm_page.get_location_field().send_keys("United")
        self.verify_link_presence("United States of America")
        confirm_page.get_search_suggestion().click()
        confirm_page.get_confirm_box().click()
        confirm_page.get_checkout_btn().click()

        success_text = confirm_page.get_success_text().text

        assert "Success! Thank you!" in success_text
