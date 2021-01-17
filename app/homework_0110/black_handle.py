# -*- coding:utf-8 -*-
__author__ = "leo"

import logging

import allure

logging.basicConfig(level=logging.INFO)


def black_wrapper(func):
    def run(*args, **kwargs):
        base_page = args[0]
        try:
            # 添加日志
            logging.info("start find : \nargs: " + str(args) + "\nkwargs: " + str(kwargs))
            return func(*args, **kwargs)
        except Exception as e:
            base_page.driver.implicitly_wait(2)
            base_page.screenshot("tmp.png")
            with open("./tmp.png", "rb") as f:
                picture = f.read()

            allure.attach(picture, attachment_type=allure.attachment_type.PNG)

            for black in base_page.black_list:
                elements = base_page.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return func(*args, **kwargs)
            raise e

    return run
