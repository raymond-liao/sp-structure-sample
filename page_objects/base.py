# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import logging
import datetime

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # wait the element visible for get
    def wait_element_visible(self, locator, doc_name="base", timeout=10, frequency=0.5):
        logging.info("Waiting for element {} visible".format(locator))

        try:
            # Record the start time of this waiting
            start = datetime.datetime.now()
            wait = WebDriverWait(self.driver, timeout, frequency)
            element = wait.until(expected_conditions.visibility_of_element_located(locator))
            # Record the end time of this waiting
            end = datetime.datetime.now()
            logging.info("start waiting: {}，end waiting: {}，waiting time: {}".format(start, end, end - start))
            return element
        except Exception as error:
            logging.exception("Waiting for element {} visible failed with an exception: {}".format(locator, error))
            self.save_web_screenshot(doc_name)
            raise

    # file_name: the name of the screenshot file
    def save_web_screenshot(self, file_name):
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filepath = "./reports/screenshots/{}_{}.png".format(file_name, now)
        try:
            self.driver.save_screenshot(filepath)
            logging.info("save_web_screenshot success: {}".format(filepath))
        except Exception as error:
            logging.exception("save_web_screenshot failed with an exception: {}".format(error))
            raise

    def input_text(self, locator, doc_name="base", *args):
        element = self.wait_element_visible(locator, doc_name)

        try:
            element.clear()
            element.send_keys(*args)
        except Exception as error:
            logging.exception("Input text {} failed with an exception: {}".format(*args, error))
            self.save_web_screenshot(doc_name)
            raise

    def submit(self, locator, doc_name="base"):
        element = self.wait_element_visible(locator, doc_name)
        try:
            element.send_keys(Keys.RETURN)
            # element.submit()
        except Exception as error:
            logging.exception("Submit failed with an exception: {}".format(error))
            self.save_web_screenshot(doc_name)
            raise

    # 获取文本内值
    def get_element_text(self, locator, doc_name="base"):
        ele = self.get_element(locator, doc_name)
        try:
            text = ele.text

            logging.info("获取元素的文本为：{}".format(text))
            return text
        except Exception as error:
            logging.exception("获取文本失败: {}".format(error))
            self.save_web_screenshot(doc_name)
            raise

    # 函数找元素
    def get_element(self, locator, doc_name="base"):
        logging.info("查找元素{}".format(doc_name))
        try:
            ele = self.driver.find_element(*locator)
            return ele
        except Exception as error:
            # 日志
            logging.exception("查找元素失败: {}".format(error))
            # 截图
            self.save_web_screenshot(doc_name)
            raise

    # 点击元素
    def click_element(self, locator, doc_name="base"):
        # 1、等待元素可见
        self.wait_element_visible(locator, doc_name, timeout=10)
        # 2、查找到元素
        ele = self.get_element(locator, doc_name)
        # 3、再点击元素
        try:
            ele.click()
        except Exception as error:
            logging.exception("元素点击失败: {}".format(error))
            self.save_web_screenshot(doc_name)
            raise
