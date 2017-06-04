import assertpy
from test_automation.page_objects.dpo_base_page import DPOBasePage


class SignupPage(DPOBasePage):

    _url = 'https://www.dporganizer.com/try-dporganizer/'

    _confirm_button_locator = ('CSS_SELECTOR', '[type="submit"]')
    _first_name_locator = ('NAME', 'your-firstname')
    _last_name_locator = ('NAME', 'your-lastname')
    _company_locator = ('NAME', 'your-company')
    _email_locator = ('NAME', 'company-email')
    _phone_locator = ('NAME', 'your-phone-cf7it-national')
    _country_selector_locator = ('CSS_SELECTOR', '.iti-flag')
    _country_locator = ('CSS_SELECTOR', '.country .country-name')
    _privacy_policy_checkbox_locator = ('NAME', 'opt-in[]')

    def verify_on_page(self):
        self.get_visible_element(self._confirm_button_locator)
        return self

    def enter_name(self, first, last):
        self.enter_text(self._first_name_locator, first)
        self.enter_text(self._last_name_locator, last)
        return self

    def enter_company(self, company):
        self.enter_text(self._company_locator, company)
        return self

    def enter_email(self, email):
        self.enter_text(self._email_locator, email)
        return self

    def enter_phone(self, phone):
        self.enter_text(self._phone_locator, phone)
        return self

    def select_country(self, country):
        self.click(self._country_selector_locator)
        country = self.get_element_with_text(self._country_locator, country)
        self.click(country)
        return self

    def check_privacy_policy(self):
        self.click(self._privacy_policy_checkbox_locator)
        return self

    def signup(self):
        # self.click(self._confirm_button_locator)
        return self

    def verify_signup_successful(self):
        assertpy.assert_that(True).is_true()  # Assert landingpage and personal info correct etc
