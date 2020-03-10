# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def webdriver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    else:
        raise ValueError("Unknowns browser for webdriver: ", request.param)

    # custom window size
    # web_driver.maximize_window()
    # web_driver.fullscreen_window()
    # web_driver.minimize_window()
    # web_driver.set_window_size(800, 800)

    request.cls.driver = web_driver
    yield
    web_driver.close()
