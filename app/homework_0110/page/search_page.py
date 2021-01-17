# -*- coding:utf-8 -*-
__author__ = "leo"

import yaml
from appium.webdriver.common.mobileby import MobileBy

from app.homework_0110.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        # self.find_and_send(
        #     MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", "小米"
        # )

        self.load_yaml("../page/search.yml")

        self.quit_after(3)
        return True
