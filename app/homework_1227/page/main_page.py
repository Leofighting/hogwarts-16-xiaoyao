# -*- coding:utf-8 -*-
__author__ = "leo"

from appium.webdriver.common.mobileby import MobileBy

from app.homework_1227.page.address_list_page import AddressListPage
from app.homework_1227.page.base_page import BasePage


class MainPage(BasePage):
    """
    首页
    """

    def goto_address(self):
        """
        进入通讯录
        :return:
        """
        self.find_and_click(
            MobileBy.XPATH,
            "//*[contains(@text, '通讯录') and @resource-id='com.tencent.wework:id/elq']",
        )
        return AddressListPage(self.driver)
