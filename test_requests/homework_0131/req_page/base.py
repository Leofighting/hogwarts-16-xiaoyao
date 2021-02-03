# -*- coding:utf-8 -*-
__author__ = "leo"

import requests
from requests import Session


class Base:
    def __init__(self):
        self.s = Session()
        self.corpid = "ww07529cf4079a789c"
        self.corpsecret = "Efd6TAMqCZMfWt10zi4QqJKjQK1yG6i5X6N-fFfxqU0"
        self.s.params["access_token"] = self.get_token().get("access_token")

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret

        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.get(url=url, params=params)
        return r.json()
