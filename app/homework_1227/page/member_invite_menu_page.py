# -*- coding:utf-8 -*-
__author__ = "leo"

from appium.webdriver.common.mobileby import MobileBy

from app.homework_1227.page.base_page import BasePage
from app.homework_1227.page.contact_add_page import ContactAdd


class MemberInviteMenuPage(BasePage):
    """
    添加成员页面
    """

    def add_member_manually(self):
        """
        点击手动添加成员
        :return:
        """
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAdd(self.driver)