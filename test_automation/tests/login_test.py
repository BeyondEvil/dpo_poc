# -*- coding: utf-8 -*-
from test_automation.page_objects.login_page import LoginPage


def test_successful_login(driver):
    LoginPage(driver).\
        go_to_page().\
        login('jimbrannlund@fastmail.com', 'password').\
        verify_login_successful()


def test_incorrect_credentials(driver):
    LoginPage(driver).\
        go_to_page().\
        login('jimbrannlund@fastmail.com', 'password').\
        verify_login_unsuccessful()
