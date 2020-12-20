# -*- coding:utf-8 -*-
__author__ = "leo"

import pytest

from python_homework.homework_1209.calculator import Calculator


@pytest.fixture(scope="module")
def setup_fixture():
    """
    整个类开始之前执行一次
    :return:
    """
    calc = Calculator()
    print("开始计算")
    yield calc
    print("结束计算")
