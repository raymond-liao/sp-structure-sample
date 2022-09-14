# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome"], scope="class")
def webdriver_init(request):
    if request.param == "chrome":
        service = Service(executable_path="./chromedriver")
        web_driver = webdriver.Chrome(service=service)

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.set_capability("browserVersion", "67")
        # chrome_options.set_capability("platformName", "Windows XP")
        # web_driver = webdriver.Remote(
        #     command_executor="http://127.0.0.1:4444",
        #     options=chrome_options
        # )
        # web_driver.get("https://www.baidu.com")
        # print(web_driver.title)
        # web_driver.quit()
    elif request.param == "firefox":
        service = Service(executable_path="./geckodriver")
        web_driver = webdriver.Firefox(service=service)
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
