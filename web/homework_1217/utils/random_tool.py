# -*- coding:utf-8 -*-
__author__ = "leo"

from faker import Faker, Factory


class RandomTool:
    def __init__(self):
        self.fake = Faker("zh_CN")
        self.factory = Factory.create()

    def create_username(self):
        username = self.factory.name()
        return username

    def create_number(self):
        number = self.fake.random_int()
        return number

    def create_phone(self):
        phone = self.fake.phone_number()
        return phone

    def create_email(self):
        email = self.fake.email()
        return email


# print(create_username())
a = RandomTool()
print(a.create_phone())
