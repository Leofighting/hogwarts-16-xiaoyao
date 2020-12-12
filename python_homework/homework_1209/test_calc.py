import pytest
import yaml

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
        self.calc = Calculator()
        print("开始计算")

    def teardown_class(self):
        """
        整个类结束后执行一次
        :return:
        """
        print("结束计算")

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["add"],
                             ids=["整数", "小数", "大整数"])
    def test_add(self, a, b, expect):
        """测试加法正向用例"""
        result = self.calc.add_func(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["add_exception"],
                             ids=["字符串"])
    def test_add_exception(self, a, b, expect):
        """测试加法异常用例"""
        with pytest.raises(Exception) as e:
            self.calc.add_func(a, b)
        assert expect in str(e.value)

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["sub"],
                             ids=["整数", "小数", "大整数"])
    def test_sub(self, a, b, expect):
        """测试减法正向用例"""
        result = self.calc.sub_func(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["sub_exception"],
                             ids=["字符串"])
    def test_sub_exception(self, a, b, expect):
        """测试减法异常用例"""
        with pytest.raises(Exception) as e:
            self.calc.sub_func(a, b)
        assert expect in str(e.value)

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["mul"],
                             ids=["整数", "小数", "大整数"])
    def test_mul(self, a, b, expect):
        """测试乘法正向用例"""
        result = self.calc.mul_func(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["mul_exception"],
                             ids=["字符串"])
    def test_mul_exception(self, a, b, expect):
        """测试乘法异常用例"""
        with pytest.raises(Exception) as e:
            self.calc.mul_func(a, b)
        assert expect in str(e.value)

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["div"],
                             ids=["整数", "小数", "大整数"])
    def test_div(self, a, b, expect):
        """测试除法正向用例"""
        result = self.calc.div_func(a, b)
        assert result == expect

    @pytest.mark.parametrize("a, b, expect",
                             yaml.safe_load(open("./data/calc_data.yml", encoding="utf-8"))["div_exception"],
                             ids=["字符串", "除数为0"])
    def test_div_exception(self, a, b, expect):
        """测试除法异常用例"""
        with pytest.raises(Exception) as e:
            self.calc.div_func(a, b)
        assert expect in str(e.value)
