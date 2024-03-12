import pytest
from TestData.home_page_data import HomePageData
from pages.home import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.browser)
        log.info(f"First name: {get_data["first_name"]}")
        home_page.get_name().send_keys(get_data["first_name"])
        log.info(f"Email: {get_data["email"]}")
        home_page.get_email().send_keys(get_data["email"])
        log.info(f"Password: {get_data["password"]}")
        home_page.get_password().send_keys(get_data["password"])
        home_page.get_checkbox().click()
        log.info(f"Gender: {get_data["gender"]}")
        self.select_option_by_text(home_page.get_gender(), get_data["gender"])
        home_page.get_employment().click()
        log.info(f"Date of birth: {get_data["birthdate"]}")
        home_page.get_birth_date().send_keys(get_data["birthdate"])
        home_page.submit_form().click()

        alert_text = home_page.get_success_message().text
        log.info(f"Message received from application is {alert_text}")

        assert "Success" in alert_text

        self.browser.refresh()

    @pytest.fixture(params=HomePageData.test_home_page_data)
    def get_data(self, request):
        return request.param
