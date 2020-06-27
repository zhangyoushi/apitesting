import json
from time import sleep

import requests
import unittest
import config.settings as a
import common.Login
import common.Common
import allure


@allure.feature('test_CreateContact')
class TestTenantContact(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.token = common.Login.login()
        cls.header = {
            'Authorization': cls.token,
            'content-type': 'application/json; charset=utf-8'
        }

    # 新建租客联系人姓名必填
    @allure.story('createContact_need_name')
    def test_name(self):
        path = '/web/tenant-contacts'

        data = {
            "address": "string",
            "companyName": "string",
            "defaultContact": False,
            "email": "123@qq.com",
            "name": "",
            "tel": "17826805813",
            "tenantId": 0
        }

        header = {
            'Authorization': self.token,
            'content-type': 'application/json; charset=utf-8'
        }

        res = requests.post(a.BASE_URL + path, json=data, headers=header)

        assert res.status_code == 400
        assert json.loads(res.text)['error'] == '姓名不能为空'
        sleep(1)

    # 新建租客联系人手机号必须为11位数字
    @allure.story('createContact_tel_need_11numbers')
    def test_tel(self):
        path = '/web/tenant-contacts'

        data ={
            "address": "string",
            "companyName": "string",
            "defaultContact": False,
            "email": "string@yu.com",
            "name": "string",
            "tel": "string",
            "tenantId": 0
        }

        res = requests.post(a.BASE_URL+path, json=data, headers=self.header)

        assert res.status_code == 400
        assert json.loads(res.text)['error'] == '手机号码长度必须为11位'

    # 新建租客联系人邮箱必须符合邮箱格式
    @allure.story('createContact_need_correct_email')
    def test_email(self):
        path = '/web/tenant-contacts'

        data = {
            "address": "string",
            "companyName": "string",
            "defaultContact": False,
            "email": "string",
            "name": "string",
            "tel": "17826805813",
            "tenantId": 0
        }

        res = requests.post(a.BASE_URL + path, json=data, headers=self.header)

        assert res.status_code == 400
        assert json.loads(res.text)['error'] == '邮箱格式不正确'
        sleep(1)

    # 新建租客联系人住址必须小于200字符
    @allure.story('createContact_address')
    def test_address(self):
        path = '/web/tenant-contacts'
        address = common.Common.creat_str()

        data = {
            "address": address,
            "companyName": "string",
            "defaultContact": False,
            "email": "string@ab.com",
            "name": "string",
            "tel": "17826805813",
            "tenantId": 0
        }

        res = requests.post(a.BASE_URL + path, json=data, headers=self.header)

        assert res.status_code == 400
        assert json.loads(res.text)['error'] == '地址最多不能超过200'

    # 新建租客联系
    @allure.story('test_createContact')
    def test_create_contacts(self):
        path = '/web/tenant-contacts'

        data = {
            "address": "string",
            "companyName": "string",
            "defaultContact": False,
            "email": "string@ab.com",
            "name": "API测试",
            "tel": "17826805813",
            "tenantId": 0
        }

        res = requests.post(a.BASE_URL + path, json=data, headers=self.header)

        assert res.status_code == 201
