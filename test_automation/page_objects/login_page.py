import assertpy
from test_automation.page_objects.dpo_base_page import DPOBasePage


class LoginPage(DPOBasePage):

    _url = 'https://app.dporganizer.com/'

    _login_button_locator = ('CSS_SELECTOR', '.btn-success')
    _email_locator = ('ID', 'email')
    _password_locator = ('ID', 'password')
    _login_alert_locator = ('CSS_SELECTOR', '.alert-dismissable')

    def verify_on_page(self):
        self.get_visible_element(self._login_button_locator)
        return self

    def login(self, email, password):
        self.enter_text(self._email_locator, email)
        self.enter_text(self._password_locator, password)
        self.click(self._login_button_locator)
        return self

    def verify_login_successful(self):
        assertpy.assert_that(True).is_true()

    def verify_login_unsuccessful(self):
        assertpy.assert_that(self.get_text(self._login_alert_locator)).contains('Login attempt was unsuccessful, '
                                                                                'please try again.')
