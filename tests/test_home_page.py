from pages.home import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self):
        home_page = HomePage(self.browser)
        home_page.get_name().send_keys("Nick")
        home_page.get_email().send_keys("nick_cramer@outlook.com")
        home_page.get_password().send_keys("password")
        home_page.get_checkbox().click()
        self.select_option_by_text(home_page.get_gender(), "Male")
        home_page.get_employment().click()
        home_page.get_birth_date().send_keys("07141994")
        home_page.submit_form().click()

        alert_text = home_page.get_success_message().text

        assert "Success" in alert_text
