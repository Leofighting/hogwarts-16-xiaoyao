# -*- coding:utf-8 -*-
__author__ = "leo"

import yaml
from appium.webdriver.common.mobileby import MobileBy

from app.homework_0110.page.base_page import BasePage
from app.homework_0110.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']")
        self.load_yaml("../page/main.yml")

        return MarketPage(self.driver)
