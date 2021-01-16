# -*- coding:utf-8 -*-
__author__ = "leo"


def black_wrapper(func):
    def run(*args, **kwargs):
        base_page = args[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            base_page.driver.implicitly_wait(10)
            for black in base_page.black_list:
                elements = base_page.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return func(*args, **kwargs)
            raise e

    return run
