# -*- coding:utf-8 -*-
__author__ = "leo"

import time

import yaml
from selenium import webdriver


def save_cookie():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    time.sleep(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    cookies = driver.get_cookies()
    # print(cookies)
    with open("E:\\hogwarts_16\\project\\hogwarts-16-xiaoyao\\web\\homework_1220\\data\\cookies.yml",
              "w",
              encoding="utf-8") as file:
        yaml.dump(cookies, file)

    driver.quit()


def get_cookies(driver):
    with open("E:\\hogwarts_16\\project\\hogwarts-16-xiaoyao\\web\\homework_1220\\data\\cookies.yml",
              encoding="utf-8") as file:
        yaml_date = yaml.safe_load(file)
        for cookie in yaml_date:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(2)


# save_cookie()
