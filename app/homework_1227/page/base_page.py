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

    def wait_for(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def quit_after(self, timeout):
        time.sleep(timeout)
        self.driver.quit()