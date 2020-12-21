# -*- coding:utf-8 -*-
__author__ = "leo"

import yaml


def get_cookies(driver):
    with open("./data/cookies.yml", encoding="utf-8") as file:
        yaml_date = yaml.safe_load(file)
        for cookie in yaml_date:
            driver.add_cookie(cookie)
