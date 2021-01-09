# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium import webdriver
from selenium.webdriver.common.by import By

from web.homework_1220.page.add_member import AddMember
from web.homework_1220.page.base_page import BasePage
from web.homework_1220.page.contact_page import ContactPage


class MainPage(BasePage):
    _element_add_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    _element_contact = (By.ID, "menu_contacts")

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        self.find(*self._element_add_member).click()
        return AddMember(self.driver)

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(*self._element_contact).click()
        return ContactPage(self.driver)
