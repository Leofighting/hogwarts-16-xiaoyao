# -*- coding:utf-8 -*-
__author__ = "leo"

import yaml


def get_data(path, key):
    with open(path, encoding="utf-8") as file:
        data = yaml.safe_load(file)
        return data[key]
