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

    def create_id(self):
        number = self.fake.random_int()
        return number

    def create_phone(self):
        phone = self.fake.phone_number()
        return phone

    def create_email(self):
        email = self.fake.email()
        return email

    def create_department_name(self):
        department_name = self.fake.company()
        return department_name


random_tool = RandomTool()
USERNAME = random_tool.create_username()
ID = random_tool.create_id()
PHONE = random_tool.create_phone()
EMAIL = random_tool.create_email()
DEPARTMENT_NAME = random_tool.create_department_name()
