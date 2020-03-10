# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import pytest

if __name__ == '__main__':
    # -v: verbose; -s: shortcut for --capture=no;
    # -m: only run tests matching given mark expression. example: -m 'mark1 and not mark2';
    # --html=path: create html report file at given path.
    # pytest.main(["-v", "-s", "-m", "smoke", "--html=./reports/smoke_tests_report.html"])
    pytest.main(["-v", "-s", "-m", "sample", "--html=./reports/sample_tests_report.html"])
