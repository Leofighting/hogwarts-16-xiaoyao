# -*- coding:utf-8 -*-
__author__ = "leo"

import time

import pytest

from web.homework_1220.page.main_page import MainPage
from web.homework_1220.utils.random_tool import USERNAME, ID, PHONE, EMAIL


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        time.sleep(5)
        self.main.quit()

    @pytest.mark.parametrize(
        "username, acctid, phone, email",
        (
            [
                USERNAME,
                ID,
                PHONE,
                EMAIL,
            ],
        ),
    )
    def test_add_member(self, username, acctid, phone, email):
        """
        主页添加成员测试用例
        :return:
        """
        res = (
            self.main.goto_add_member()
            .add_member(username, acctid, phone, email)
            .get_member()
        )
        assert USERNAME in res

    @pytest.mark.parametrize(
        "username, acctid, phone, email, expected_res",
        (
            [USERNAME, ID, "13362529108", EMAIL, "该手机"],
            [USERNAME, "8517", PHONE, EMAIL, "该帐号"],
        ),
    )
    def test_add_member_fail(self, username, acctid, phone, email, expected_res):
        res = self.main.goto_add_member().add_member_fail(
            username, acctid, phone, email
        )
        # print(res)
        try:
            for i in res:
                # print(expected_res, i, type(i))
                if expected_res in i:
                    assert True
        except:
            assert False

    def test_add_member_by_contact(self):
        """
        通过通讯录页面添加成员测试用例
        :return:
        """
        res = self.main.goto_contact().goto_add_member().add_member().get_member()
        assert USERNAME in res
