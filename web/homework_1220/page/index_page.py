# -*- coding:utf-8 -*-
__author__ = "leo"

from web.homework_1220.page.login_page import LoginPage
from web.homework_1220.page.register_page import RegisterPage


class IndexPage:
    def goto_login(self):
        """跳转到登录页面"""
        return LoginPage()

    def goto_register(self):
        """跳转到注册页面"""
        return RegisterPage()
