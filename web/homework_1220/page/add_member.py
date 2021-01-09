# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from web.homework_1220.page.base_page import BasePage


class AddMember(BasePage):
    _element_username = (By.ID, "username")
    _element_acctid = (By.ID, "memberAdd_acctid")
    _element_phone = (By.ID, "memberAdd_phone")
    _element_mail = (By.ID, "memberAdd_mail")
    _element_save = (By.CSS_SELECTOR, ".js_btn_save")
    _element_error_message = (By.XPATH, "//div[@class='ww_telInput']/../div[@class='ww_inputWithTips_tips']")
    _elements_error = (By.CSS_SELECTOR, ".ww_inputWithTips_tips")

    def add_member(self, username, acctid, phone, email):
        """
        添加成员操作
        :return:
        """
        from web.homework_1220.page.contact_page import ContactPage
        self.driver.find_element(*self._element_username).send_keys(username)
        self.driver.find_element(*self._element_acctid).send_keys(acctid)
        self.driver.find_element(*self._element_phone).send_keys(phone)
        self.driver.find_element(*self._element_mail).send_keys(email)
        self.driver.find_element(*self._element_save).click()
        return ContactPage(self.driver)

    def add_member_fail(self, username, acctid, phone, email):
        """
        添加成员失败
        :return:
        """
        self.find(*self._element_username).send_keys(username)
        self.find(*self._element_acctid).send_keys(acctid)
        self.find(*self._element_phone).send_keys(phone)
        self.find(*self._element_mail).send_keys(email)
        self.find(*self._element_save).click()
        time.sleep(1)
        # error_message = self.get_error_message(self._element_error_message)
        error_elements = self.finds(*self._elements_error)
        error_list = [element.text for element in error_elements]
        return error_list

    def get_error_message(self, locator):
        error_message = self.find(*locator).text
        return error_message
