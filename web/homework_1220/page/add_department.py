# -*- coding:utf-8 -*-
__author__ = "leo"

from selenium.webdriver.common.by import By

from web.homework_1220.page.base_page import BasePage

from web.homework_1220.utils.random_tool import DEPARTMENT_NAME


class AddDepartment(BasePage):
    _element_name = (By.NAME, "name")
    _element_department1 = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _element_department2 = (
        By.XPATH,
        "//div[@class='member_tag_dialog_inputDlg']//li[@aria-level='1']/a",
    )
    _element_submit = (By.XPATH, "//a[@d_ck='submit']")

    def add_department(self):
        """
        添加部门
        :return:
        """
        from web.homework_1220.page.contact_page import ContactPage

        self.find(*self._element_name).send_keys(DEPARTMENT_NAME)
        self.find(*self._element_department1).click()
        self.find(*self._element_department2).click()
        self.find(*self._element_submit).click()
        return ContactPage(self.driver)
