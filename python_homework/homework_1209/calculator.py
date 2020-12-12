from decimal import Decimal


class Calculator:
    def add_func(self, a, b):
        """
        加法
        :param a: 加数
        :param b: 加数
        :return: 和
        """
        # 判断 a, b 是否为整数或者小数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            return result
        raise TypeError("a,b 都必须为整数或者小数！")

    def sub_func(self, a, b):
        """
        减法
        :param a: 被减数
        :param b: 减数
        :return: 差
        """
        # 判断 a, b 是否为整数或者小数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a - b
            return result
        raise TypeError("a,b 都必须为整数或者小数！")

    def mul_func(self, a, b):
        """
        乘法
        :param a: 乘数
        :param b: 乘数
        :return: 积
        """
        # 判断 a, b 是否为整数或者小数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a * b
            return result
        raise TypeError("a,b 都必须为整数或者小数！")

    def div_func(self, a, b):
        """
        除法
        :param a: 被除数
        :param b: 除数
        :return: 商
        """
        # 判断 a, b 是否为整数或者小数
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            # 判断 b 是否为 0
            if b == 0:
                raise ZeroDivisionError("除数不能为 0 ！")
            result = a / b
            return result
        raise TypeError("a,b 都必须为整数或者小数！")
