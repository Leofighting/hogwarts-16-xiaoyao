# -*- coding:utf-8 -*-
__author__ = "leo"

from appium.webdriver.common.mobileby import MobileBy

from app.homework_0107.page.base_page import BasePage
from app.homework_0107.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find_and_click(
            MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"
        )

        return SearchPage(self.driver)
