# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import pytest
from selenium.webdriver.common.keys import Keys

from page_objects.login import LoginPage
from test_cases.test_basic import WebBasicTest
from test_datas.login_data import LoginData


@pytest.mark.smoke
class TestLogin(WebBasicTest):
    @pytest.fixture()
    def open_page(self):
        self.driver.get(LoginData.global_url)
        print(self.driver.title)
        self.page = LoginPage(self.driver)

    @pytest.mark.usefixtures("open_page")
    def test_login(self):
        assert "Butter - Global Service" in self.driver.title
        self.page.deeplink()
        self.page.login()
        assert "No results found." not in self.driver.page_source
