# -*- coding:utf-8 -*-
__author__ = "leo"

from appium.webdriver.common.mobileby import MobileBy

from app.homework_0107.page.base_page import BasePage
from app.homework_0107.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']")

        return MarketPage(self.driver)
