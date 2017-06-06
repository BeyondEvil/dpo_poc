# -*- coding: utf-8 -*-
import pytest
from test_automation.page_objects.login_page import LoginPage

pytestmark = pytest.mark.tags("login")

module_setup_data = [{'User': [{'name': 'Jim', 'email': 'jimbrannlund@fastmail.com'}]}]


def test_successful_login(test_db, driver):
    user = test_db.get('User', 'Jim')
    LoginPage(driver).\
        go_to_page().\
        login(user.email, user.password).\
        verify_login_successful()


def test_incorrect_credentials(test_db, driver):
    user = test_db.get('User', 'Jim')
    LoginPage(driver).\
        go_to_page().\
        login(user.email, user.password).\
        verify_login_unsuccessful()
