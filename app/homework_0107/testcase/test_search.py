# -*- coding:utf-8 -*-
__author__ = "leo"

from app.homework_0107.page.app import App


class TestSearch:
    def setup(self):
        self.app = App()
        self.app.start()

    def test_search(self):
        self.app.goto_main().goto_market().goto_search().search()
