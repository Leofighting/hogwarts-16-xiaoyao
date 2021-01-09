# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium.webdriver.common.by import By

from web.homework_1220.page.add_department import AddDepartment
from web.homework_1220.page.add_member import AddMember
from web.homework_1220.page.base_page import BasePage


class ContactPage(BasePage):

    _element_add = (By.CSS_SELECTOR, '.js_create_dropdown')
    _element_add_department = (By.CSS_SELECTOR, '.js_create_party')
    _elements_member = (By.XPATH, "//tr[contains(@class, 'member_colRight_memberTable_tr_Inactive')]/td[2]")
    _element_add_member = (By.LINK_TEXT, "添加成员")
    _elements_department = (By.CSS_SELECTOR, ".jstree-anchor")

    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        self.find(*self._element_add_member).click()
        return AddMember(self.driver)

    def goto_add_department(self):
        """
        添加部门
        :return:
        """
        self.find(*self._element_add).click()
        self.find(*self._element_add_department).click()
        return AddDepartment(self.driver)

    def get_member(self):
        """
        获取员工列表，用于做断言信息
        :return:
        """
        elements = self.finds(*self._elements_member)
        member_list = []

        for element in elements:
            member_list.append(element.text)

        return member_list

    def get_department(self):
        """
        获取部门列表，用于做断言信息
        :return:
        """
        time.sleep(1)
        elements = self.finds(*self._elements_department)
        department_list = []

        for element in elements:
            department_list.append(element.text)

        return department_list
