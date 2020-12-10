class Calculator:
    def add_func(self, a, b):
        """
        加法
        :param a: 加数
        :param b: 加数
        :return: 和
        """
        return a + b

    def sub_func(self, a, b):
        """
        减法
        :param a: 被减数
        :param b: 减数
        :return: 差
        """
        return a - b

    def mul_func(self, a, b):
        """
        乘法
        :param a: 乘数
        :param b: 乘数
        :return: 积
        """
        return a * b

    def div_func(self, a, b):
        """
        除法
        :param a: 被除数
        :param b: 除数
        :return: 商
        """
        try:
            return a / b
        except:
            raise ZeroDivisionError


# ca = Calculator()
# print(ca.div_func(4, 2))