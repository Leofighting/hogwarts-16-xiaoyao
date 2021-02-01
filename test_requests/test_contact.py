# -*- coding:utf-8 -*-
__author__ = "leo"

import requests

from test_requests.utils.random_tool import USERNAME, PHONE, ID


def get_token():
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    params = {
        "corpid": "ww07529cf4079a789c",
        "corpsecret": "Efd6TAMqCZMfWt10zi4QqJKjQK1yG6i5X6N-fFfxqU0"
    }
    r = requests.get(url=url, params=params)
    # print(r.json())
    # assert r.json()["errcode"] == 0
    token = r.json()['access_token']
    return token


def test_defect_member():
    get_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
    get_member_params = {
        "access_token": get_token(),
        "userid": "22"
    }

    r1 = requests.get(url=get_member_url, params=get_member_params)
    print(r1.json())
    assert "Adam Cabrera" == r1.json()["name"]


def test_update_member():
    update_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={}".format(get_token())
    data = {
        "userid": "22",
        "name": USERNAME,
        "mobile": PHONE,
    }
    print(USERNAME, PHONE)
    r = requests.post(url=update_member_url, json=data)
    print(r.json())


def test_create_member():
    create_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={}".format(get_token())

    crete_member_data = {
        "userid": str(ID),
        "name": USERNAME,
        "mobile": "+86 "+PHONE,
        "department": [2]
    }
    r = requests.post(url=create_member_url, json=crete_member_data)
    print(r.json())


def test_delete_member():
    delete_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
    delete_member_params = {
        "access_token": get_token(),
        "userid": "22"
    }
    r = requests.get(url=delete_member_url, params=delete_member_params)
    print(r.json())
