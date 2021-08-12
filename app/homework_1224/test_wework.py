# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = dict()
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["settings[waitForIdleTimeout]"] = 0  # 设置页面空闲等待时间

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_clock_in(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 下拉直到找到 “打卡”
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector()."
            "scrollable(true).instance(0))."
            "scrollIntoView(new UiSelector()."
            'text("打卡").instance(0));',
        ).click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()

        locator = (MobileBy.ID, "com.tencent.wework:id/pt")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

        assert "外出打卡成功" in self.driver.page_source
