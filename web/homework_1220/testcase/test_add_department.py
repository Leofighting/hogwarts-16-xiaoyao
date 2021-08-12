# -*- coding:utf-8 -*-
__author__ = "leo"

from web.homework_1220.page.main_page import MainPage
from web.homework_1220.utils.random_tool import DEPARTMENT_NAME


class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        """
        添加部门测试用例
        :return:
        """
        res = (
            self.main.goto_contact()
            .goto_add_department()
            .add_department()
            .get_department()
        )
        assert DEPARTMENT_NAME in res
