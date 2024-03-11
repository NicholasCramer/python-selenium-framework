from selenium.webdriver.common.by import By

from pages.shop import ShopPage


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email = (By.NAME, "email")
    name = (By.CSS_SELECTOR, "input[name='name']")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    employment_status = (By.CSS_SELECTOR, "input[value='option1']")
    birth_date = (By.CSS_SELECTOR, "input[name='bday']")
    form_submit_btn = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def navigate_to_shop(self):
        self.browser.find_element(*HomePage.shop).click()
        shop_page = ShopPage(self.browser)
        return shop_page

    def get_name(self):
        return self.browser.find_element(*HomePage.name)

    def get_email(self):
        return self.browser.find_element(*HomePage.email)

    def get_password(self):
        return self.browser.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.browser.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.browser.find_element(*HomePage.gender)

    def get_employment(self):
        return self.browser.find_element(*HomePage.employment_status)

    def get_birth_date(self):
        return self.browser.find_element(*HomePage.birth_date)

    def submit_form(self):
        return self.browser.find_element(*HomePage.form_submit_btn)

    def get_success_message(self):
        return self.browser.find_element(*HomePage.success_message)
