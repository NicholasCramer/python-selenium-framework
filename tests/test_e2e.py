import pytest
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestOne(BaseClass):

    def test_e2e(self):

        self.browser.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        product_elements = self.browser.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in product_elements:
            product_name = product.find_element(By.XPATH, "div/h4/a").text
            if product_name == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.browser.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
        self.browser.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        self.browser.find_element(By.ID, "country").send_keys("United")
        wait = WebDriverWait(self.browser, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))
        self.browser.find_element(By.LINK_TEXT, "United States of America").click()
        self.browser.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()
        self.browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        success_text = self.browser.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in success_text

