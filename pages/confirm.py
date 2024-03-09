from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:

    def __init__(self, browser):
        self.browser = browser

    location_field = (By.ID, "country")
    search_suggestion = (By.LINK_TEXT, "United States of America")
    confirm_check_box = (By.CSS_SELECTOR, ".checkbox.checkbox-primary")
    checkout_btn = (By.CSS_SELECTOR, "input[type='submit']")
    success_text = (By.CLASS_NAME, "alert-success")

    def get_location_field(self):
        return self.browser.find_element(*ConfirmPage.location_field)

    def get_search_suggestion(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "United States of America")))
        return self.browser.find_element(*ConfirmPage.search_suggestion)

    def get_confirm_box(self):
        return self.browser.find_element(*ConfirmPage.confirm_check_box)

    def get_checkout_btn(self):
        return self.browser.find_element(*ConfirmPage.checkout_btn)

    def get_success_text(self):
        return self.browser.find_element(*ConfirmPage.success_text)
