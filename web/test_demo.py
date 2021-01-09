# -*- coding:utf-8 -*-
__author__ = "leo"

import time

import yaml
from selenium import webdriver


class TestWework:
    def test_demo(self):
        opt = webdriver.ChromeOptions()
        # 设置 debug 地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        time.sleep(10)
        driver.find_element_by_id("menu_contacts").click()
        print(driver.get_cookies())


def test_cookie():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")

    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
                'value': 'XWPFNhloZ-5BXk8lrXP9PBnlGCO3TApQS_eqo7R1pxSY_6hx4F3B_BbPru8P38niOE1HD24tEeZTJeco5f9Cz5D-YM1u5x3a-kMU2wNJzHw2i06Rvdr17Fxw952NwCe2cf91Dk54tCUtODonmRFI0d2cXtPFSqkzA8KzjHugbXnbkYgbHNJzEb_bb5jitUZ4S9aAkOGRgeWQ7cmyYwdVBTKvqlMjRglDUq5cQkSe6NS776Pa_AM-r6xLJOmou3zaVQIC9ltw9yNdoeYH6cBEPA'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
                'value': '1688851976796534'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                'secure': False, 'value': '1970325128211808'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': 'xHYRzolHyge1EbFANQBNzwfJwYiHYH6Q_r4kNlboCVynpS6FYXB1n8-HzrjQ07n_'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                'value': 'a2517056'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
                'value': '30817826413212917'},
               {'domain': 'work.weixin.qq.com', 'expiry': 1608589650, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
                'secure': False, 'value': '6ipqo37'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1639742551, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
                'path': '/', 'secure': False, 'value': '0'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1611151472, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                'path': '/', 'secure': False, 'value': 'zh'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
                'value': '1688851976796534'},
               {'domain': '.qq.com', 'expiry': 1912318445, 'httpOnly': False, 'name': 'iip', 'path': '/',
                'secure': False, 'value': '0'},
               {'domain': '.qq.com', 'expiry': 1900198435, 'httpOnly': False, 'name': 'pac_uid', 'path': '/',
                'secure': False, 'value': '1_469342045'},
               {'domain': '.qq.com', 'expiry': 1644585687, 'httpOnly': False, 'name': '_ga', 'path': '/',
                'secure': False, 'value': 'GA1.2.1351510267.1581513687'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/',
                'secure': False, 'value': '469342045'},
               {'domain': '.qq.com', 'expiry': 1896167196, 'httpOnly': False, 'name': 'mobileUV', 'path': '/',
                'secure': False, 'value': '1_1700f738dea_934e7'},
               {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                'secure': False, 'value': '6a0c44305b986b7186eb10976c4a4401e87b4de993cdbdd1f5d0e51da37eb950'},
               {'domain': '.qq.com', 'expiry': 1621144523, 'httpOnly': True, 'name': 'ied_qq', 'path': '/',
                'secure': False, 'value': 'o0469342045'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
                'secure': False, 'value': '1271965696'},
               {'domain': '.qq.com', 'expiry': 1892940432, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/',
                'secure': False, 'value': '931a9fa2f2578840'},
               {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/',
                'secure': False, 'value': '/SSgBkdtEz'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
                'value': '1'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
                'value': 'direct'},
               {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
                'secure': False, 'value': '2428854886'}]

    for cookie in cookies:
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(3)

    driver.find_element_by_id("menu_contacts").click()
    print(driver.get_cookies())
    time.sleep(3)
    driver.quit()


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    # 设置 debug 地址
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)
    time.sleep(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookies = driver.get_cookies()
    # print(cookies)
    with open("cookies.yml", "w", encoding="utf-8") as file:
        yaml.dump(cookies, file)


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("cookies.yml", encoding="utf-8") as file:
        yaml_date = yaml.safe_load(file)
        for cookie in yaml_date:
            driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    time.sleep(2)
    driver.quit()
