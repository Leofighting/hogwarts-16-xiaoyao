# -*- coding:utf-8 -*-
__author__ = "leo"

import time

from selenium import webdriver

from web.homework_1217.utils.get_cookies import get_cookies
from web.homework_1217.utils.random_tool import RandomTool


def test_add_user():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    get_cookies(driver)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    driver.find_element_by_link_text("添加成员").click()

    username = RandomTool().create_username()
    driver.find_element_by_id("username").send_keys(username)
    number = RandomTool().create_number()
    driver.find_element_by_id("memberAdd_acctid").send_keys(number)

    phone = RandomTool().create_phone()
    driver.find_element_by_id("memberAdd_phone").send_keys(phone)

    email = RandomTool().create_email()
    driver.find_element_by_id("memberAdd_mail").send_keys(email)

    driver.find_element_by_xpath("//a[@class='qui_btn ww_btn js_btn_save']").click()

    elements = driver.find_elements_by_xpath("//tbody[@id='member_list']/tr/td[2]/span")
    username_list = [element.text for element in elements]
    print(username_list)
    assert username in username_list

    driver.quit()
