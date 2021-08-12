import pytest
import yaml

from .calculator import Calculator
from .utils.get_yaml_data import get_data

yaml_path = "./data/calc_data.yml"


class TestCalc:
    """
    测试 加减乘除 计算
    """

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "add"), ids=["整数", "小数", "大整数"]
    )
    def test_add(self, a, b, expect, setup_fixture):
        """测试加法正向用例"""
        result = setup_fixture.add_func(a, b)
        assert abs(result - expect) < 0.01

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "add_exception"), ids=["字符串"]
    )
    def test_add_exception(self, a, b, expect, setup_fixture):
        """测试加法异常用例"""
        with pytest.raises(Exception) as e:
            setup_fixture.add_func(a, b)
        assert expect in str(e.value)

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "sub"), ids=["整数", "小数", "大整数"]
    )
    def test_sub(self, a, b, expect, setup_fixture):
        """测试减法正向用例"""
        result = setup_fixture.sub_func(a, b)
        assert abs(result - expect) < 0.01

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "sub_exception"), ids=["字符串"]
    )
    def test_sub_exception(self, a, b, expect, setup_fixture):
        """测试减法异常用例"""
        with pytest.raises(Exception) as e:
            setup_fixture.sub_func(a, b)
        assert expect in str(e.value)

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "mul"), ids=["整数", "小数", "大整数"]
    )
    def test_mul(self, a, b, expect, setup_fixture):
        """测试乘法正向用例"""
        result = setup_fixture.mul_func(a, b)
        assert abs(result - expect) < 0.01

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "mul_exception"), ids=["字符串"]
    )
    def test_mul_exception(self, a, b, expect, setup_fixture):
        """测试乘法异常用例"""
        with pytest.raises(Exception) as e:
            setup_fixture.mul_func(a, b)
        assert expect in str(e.value)

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "div"), ids=["整数", "小数", "大整数"]
    )
    def test_div(self, a, b, expect, setup_fixture):
        """测试除法正向用例"""
        result = setup_fixture.div_func(a, b)
        assert abs(result - expect) < 0.01

    @pytest.mark.parametrize(
        "a, b, expect", get_data(yaml_path, "div_exception"), ids=["字符串", "除数为0"]
    )
    def test_div_exception(self, a, b, expect, setup_fixture):
        """测试除法异常用例"""
        with pytest.raises(Exception) as e:
            setup_fixture.div_func(a, b)
        assert expect in str(e.value)
