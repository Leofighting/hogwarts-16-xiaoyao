# -*- coding:utf-8 -*-
__author__ = "leo"


from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.homework_1220.utils.get_cookies import get_cookies


class BasePage:
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            get_cookies(self.driver)
        else:
            self.driver = base_driver

    def find(self, by, value=None):
        """
        对 find_element 封装
        :return:
        """
        if value is None:
            return self.driver.find_element(*by)
        return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        """
        对 find_elements 封装
        :return:
        """
        if value is None:
            return self.driver.find_elements(*by)
        return self.driver.find_elements(by=by, value=value)

    def wait_click(self, locator):
        WebDriverWait(self.driver).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def quit(self):
        self.driver.quit()
