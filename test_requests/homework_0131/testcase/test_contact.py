# -*- coding:utf-8 -*-
__author__ = "leo"

import pytest

from test_requests.homework_0131.req_page.contact import Contact
from test_requests.homework_0131.utils.random_tool import USERNAME, PHONE, ID


class TestContact:
    name = USERNAME
    mobile = PHONE
    user_id = str(ID)

    def setup_class(self):
        self.contact = Contact()

    @pytest.mark.parametrize(
        "corpid, secret, result",
        ([None, None, 0], ["xxx", None, 40013], [None, "11111", 40001]),
    )
    def test_token(self, corpid, secret, result):
        r = self.contact.get_token(corpid, secret)
        assert r.get("errcode") == result

    def test_create(self):
        self.contact.create_member(self.user_id, self.name, self.mobile, [3])
        try:
            result = self.contact.find_member(self.user_id)
        finally:
            self.contact.delete_member(self.user_id)
        assert self.name == result.get("name", "断言失败")

    def test_update(self):
        change_mobile = PHONE
        self.contact.create_member(self.user_id, self.name, self.mobile, [3])
        self.contact.update_member(self.user_id, self.name, change_mobile)
        try:
            result = self.contact.find_member(self.user_id)
        finally:
            self.contact.delete_member(self.user_id)
        assert result["mobile"] == change_mobile

    def test_delete(self):
        self.contact.create_member(self.user_id, self.name, self.mobile, [3])
        r = self.contact.delete_member(self.user_id)
        assert r.get("errcode") == 0

    def test_find(self):
        self.contact.create_member(self.user_id, self.name, self.mobile, [3])
        r = self.contact.find_member(self.user_id)
        assert r.get("name") == self.name
