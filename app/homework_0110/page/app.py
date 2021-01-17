# -*- coding:utf-8 -*-
__author__ = "leo"

from appium import webdriver

from app.homework_0110.page.base_page import BasePage
from app.homework_0110.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()

        # self.driver.start_recording_screen("../recording_screen/tmp.mp4")

    def goto_main(self):
        return MainPage(self.driver)
