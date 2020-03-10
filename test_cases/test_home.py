# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import pytest
from selenium.webdriver.common.keys import Keys

from page_objects.home import HomePage
from test_cases.test_basic import WebBasicTest
from test_datas.home_data import HomeData


@pytest.mark.smoke
class TestHome(WebBasicTest):
    @pytest.fixture()
    def open_page(self):
        self.driver.get(HomeData.home_url)
        print(self.driver.title)
        self.page = HomePage(self.driver)

    @pytest.mark.usefixtures("open_page")
    def test_home(self):
        assert "Python" in self.driver.title
        self.page.search()
        assert "No results found." not in self.driver.page_source
