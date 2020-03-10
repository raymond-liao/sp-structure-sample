# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

from selenium.webdriver.common.by import By


class HomePageLocators:
    home_search_input_locator = (By.NAME, 'q')
    home_search_unknown_locator = (By.NAME, 'unknown')
