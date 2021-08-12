# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def scroll_find(self, text):
        return self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR,
            "new UiScrollable(new UiSelector()."
            "scrollable(true).instance(0))."
            "scrollIntoView(new UiSelector()."
            'text("{text}").instance(0));'.format(text=text),
        )

    def scroll_find_click(self, text):
        self.scroll_find(text).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def wait_for(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
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
