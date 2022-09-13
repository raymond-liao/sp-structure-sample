# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

from selenium.webdriver.common.by import By


class LoginPageLocators:
    deeplink_page_left_img_locator = (By.XPATH, '//div[@class="left"]')

    deeplink_page_code_input_locator = (By.XPATH, '//label[@for="code"]//following-sibling::div//input')
    deeplink_next_button_locator = (By.XPATH, '//button//span[contains(text(),"Next")]')
    global_login_url_locator = (By.XPATH, '//h2[contains(text(),"global.butterglobe.com/BIPO")]')

    login_email_input_locator = (By.XPATH, '//label[@for="email"]//following-sibling::div//input')
    login_pwd_input_locator = (By.XPATH, '//label[@for="password"]//following-sibling::div//input')

    forget_pwd_button_locator = (By.XPATH, '//button//span[contains(text(),"Forget Password")]')
    sign_in_button_locator = (By.XPATH, '//button//span[contains(text(),"Sign in")]')

    terms_service_a_locator = (By.XPATH, '//a//span//em[contains(text(),"Terms of Service")]')
    privacy_policy_a_locator = (By.XPATH, '//a//span//em[contains(text(),"Privacy Policy")]')

    service_company_ltd_locator = (By.XPATH, '//div[@class="copyright"]')
