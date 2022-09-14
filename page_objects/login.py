# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

from page_locators.login_locators.login_page_locators import LoginPageLocators
from page_objects.base import BasePage
from test_datas.login_data import LoginData


class LoginPage(BasePage):
    def deeplink(self):
        doc_name = "global_deeplink"
        self.wait_element_visible(LoginPageLocators.deeplink_page_left_img_locator)

        self.input_text(LoginPageLocators.deeplink_page_code_input_locator, doc_name, LoginData.company_code)
        self.wait_element_visible(LoginPageLocators.deeplink_next_button_locator)
        self.click_element(LoginPageLocators.deeplink_next_button_locator, '点击下一步按钮')
        self.wait_element_visible(LoginPageLocators.global_login_url_locator)

    def login(self):
        doc_name = "global_login"
        self.input_text(LoginPageLocators.login_email_input_locator, doc_name, LoginData.login_email)
        self.input_text(LoginPageLocators.login_pwd_input_locator, doc_name, LoginData.login_password)
        self.wait_element_visible(LoginPageLocators.forget_pwd_button_locator)
        self.wait_element_visible(LoginPageLocators.sign_in_button_locator)
        self.wait_element_visible(LoginPageLocators.terms_service_a_locator)
        self.wait_element_visible(LoginPageLocators.privacy_policy_a_locator)
        self.wait_element_visible(LoginPageLocators.service_company_ltd_locator)

        self.click_element(LoginPageLocators.sign_in_button_locator, '点击登录按钮')
        self.wait_element_visible(LoginPageLocators.topbar_settings_locator)
        self.click_element(LoginPageLocators.topbar_settings_locator)

        self.wait_element_visible(LoginPageLocators.topbar_settings_signout_locator)
        self.click_element(LoginPageLocators.topbar_settings_signout_locator)

        self.wait_element_visible(LoginPageLocators.deeplink_page_title_locator)





