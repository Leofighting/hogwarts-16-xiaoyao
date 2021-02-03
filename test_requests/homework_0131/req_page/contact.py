# -*- coding:utf-8 -*-
__author__ = "leo"

from test_requests.homework_0131.req_page.base import Base


class Contact(Base):

    def find_member(self, user_id):
        get_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        get_member_params = {
            "userid": user_id
        }

        r = self.s.get(url=get_member_url, params=get_member_params)
        return r.json()

    def update_member(self, user_id, name, mobile, **kwargs):
        update_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
        }
        data.update(kwargs)
        r = self.s.post(url=update_member_url, json=data)
        return r.json()

    def create_member(self, user_id, name, mobile, department, **kwargs):
        create_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"

        crete_member_data = {
            "userid": user_id,
            "name": name,
            "mobile": "+86 " + mobile,
            "department": department
        }

        crete_member_data.update(kwargs)

        r = self.s.post(url=create_member_url, json=crete_member_data)
        return r.json()

    def delete_member(self, user_id):
        delete_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        delete_member_params = {
            "userid": user_id
        }
        r = self.s.get(url=delete_member_url, params=delete_member_params)
        return r.json()
