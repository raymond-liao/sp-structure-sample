# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import pytest


@pytest.mark.usefixtures("webdriver_init")
class WebBasicTest:
    page = None

