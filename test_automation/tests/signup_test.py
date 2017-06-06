# -*- coding: utf-8 -*-
import pytest
from test_automation.page_objects.signup_page import SignupPage

pytestmark = pytest.mark.tags("signup")


@pytest.mark.tags("trial", "not chrome")
def test_signup_trial(driver):
    SignupPage(driver).\
        go_to_page().\
        enter_name('Jim', 'Brannlund').\
        enter_company('MyOwn').\
        enter_email('myemail@mail.com').\
        select_country('Sweden').\
        enter_phone('+46707696100').\
        check_privacy_policy().\
        signup().\
        verify_signup_successful()
