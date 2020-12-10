import pytest
from .calculator import Calculator


class TestCalc:
    """
    测试 加减乘除 计算
    """
    def setup_class(self):
        """
        整个类开始之前执行一次
        :return:
        """
        print("开始计算")

    def teardown_class(self):
        """
        整个类结束后执行一次
        :return:
        """
        print("结束计算")

