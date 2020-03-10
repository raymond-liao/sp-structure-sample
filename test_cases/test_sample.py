import pytest


# pytest in action – test_pytest_example_1.py
def function_1(var):
    return var + 1


@pytest.mark.sample
def test_success():
    assert function_1(4) == 5


@pytest.mark.sample
def test_failure():
    assert function_1(2) == 5
