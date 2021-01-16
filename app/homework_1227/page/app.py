# -*- coding:utf-8 -*-
__author__ = "leo"

from appium import webdriver

from app.homework_1227.page.base_page import BasePage
from app.homework_1227.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = dict()
            caps["platformName"] = "Android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['settings[waitForIdleTimeout]'] = 0  # 设置页面空闲等待时间
            caps['ensureWebviewsHavePages'] = True

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return MainPage(self.driver)
