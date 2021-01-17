# -*- coding:utf-8 -*-
__author__ = "leo"

import time

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.homework_0110.black_handle import black_wrapper


class BasePage:
    FIND = "find"
    ACTION = "action"
    FIND_AND_CLICK = "find_and_click"
    FIND_AND_SEND = "find_and_send"
    CONTENT = "content"

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(MobileBy.XPATH, "//*[contains(@text, '跳过广告')]"),
                           (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    @black_wrapper
    def find(self, by, locator):
        # self.driver.save_screenshot("tmp.png")
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                                        ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        'scrollIntoView(new UiSelector().'
                                        'text("{text}").instance(0));'.format(text=text))

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def wait_for(self, by, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((by, locator))
        )

    def swipe_find(self, by, locator):
        self.driver.implicitly_wait(3)
        elements = self.finds(by, locator)

        while len(elements) == 0:
            self.driver.swipe(10, 800, 10, 300)
            elements = self.finds(by, locator)

        return elements[0]

    def swipe_find_click(self, by, locator):
        self.swipe_find(by, locator).click()

    def quit_after(self, timeout):
        time.sleep(timeout)
        self.driver.quit()

    def load_yaml(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        for step in data:
            xpath_expr = step[self.FIND]
            action = step[self.ACTION]
            if action == self.FIND_AND_CLICK:
                self.find_and_click(MobileBy.XPATH, xpath_expr)
            elif action == self.FIND_AND_SEND:
                content = step[self.CONTENT]
                self.find_and_send(MobileBy.XPATH, xpath_expr, content)

    def screenshot(self, file):
        self.driver.save_screenshot(file)
