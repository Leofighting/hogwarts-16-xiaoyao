# -*- coding:utf-8 -*-
__author__ = "leo"

from appium.webdriver.common.mobileby import MobileBy

from app.homework_1227.page.base_page import BasePage
from app.homework_1227.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    """
    通讯录
    """

    def click_add_member(self):
        """
        点击添加成员按钮
        :return:
        """
        self.swipe_find_click(MobileBy.XPATH, "//*[@text='添加成员']")
        return MemberInviteMenuPage(self.driver)
