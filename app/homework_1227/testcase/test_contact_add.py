# -*- coding:utf-8 -*-
__author__ = "leo"

from app.homework_1227.page.app import App


class TestContactAdd:
    def setup(self):
        self.app = App()
        self.app.start()

    def test_contact_add(self):
        result = self.app.goto_main().goto_address().click_add_member().add_member_manually().add_contact()
        assert result
