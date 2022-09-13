# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

from page_locators.home_locators.home_page_locators import HomePageLocators
from page_objects.base import BasePage
from test_datas.home_data import HomeData


class HomePage(BasePage):
    def search(self):
        doc_name = "home_search"
