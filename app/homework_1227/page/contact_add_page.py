# -*- coding:utf-8 -*-
__author__ = "leo"

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.homework_1227.page.base_page import BasePage
from app.homework_1227.utils.random_tool import USERNAME, PHONE


class ContactAdd(BasePage):
    """
    添加成员信息
    """

    def add_contact(self):
        """
        添加成员
        :return:
        """
        self.find_and_send(
            MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']", USERNAME)

        self.find_and_click(
            MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")

        locator = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']")

        self.wait_for(locator)

        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")

        self.find_and_send(
            MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']", PHONE)

        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")

        return True
