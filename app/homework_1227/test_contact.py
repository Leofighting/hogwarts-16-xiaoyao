# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.homework_1227.utils.random_tool import USERNAME, PHONE


class TestContact:
    def setup(self):
        caps = dict()
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["settings[waitForIdleTimeout]"] = 0  # 设置页面空闲等待时间
        caps["ensureWebviewsHavePages"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_contact(self):
        contact_element = self.driver.find_element(
            MobileBy.XPATH,
            "//*[contains(@text, '通讯录') and @resource-id='com.tencent.wework:id/elq']",
        )
        contact_element.click()
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector()."
            "scrollable(true).instance(0))."
            "scrollIntoView(new UiSelector()."
            'text("添加成员").instance(0));',
        ).click()
        handle_add_element = self.driver.find_element(
            MobileBy.XPATH, "//*[@text='手动输入添加']"
        )
        handle_add_element.click()

        self.driver.find_element(
            MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']"
        ).send_keys(USERNAME)

        self.driver.find_element(
            MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']"
        ).click()

        locator = (
            MobileBy.XPATH,
            "//*[@resource-id='com.tencent.wework:id/elq' and @text='女']",
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )

        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(
            MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']"
        ).send_keys(PHONE)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
