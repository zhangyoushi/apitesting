import json
import requests
import unittest
import config.settings as a
import common.Login
import common.Common
import allure


@allure.feature('test_Contact_Repeat')
class TestTenantContactCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.token = common.Login.login()
        common.Common.creat_tenant(cls.token, '测试重复邮箱手机号')

        cls.header = {
            'Authorization': cls.token,
            'content-type': 'application/json; charset=utf-8'
        }

        cls.DATA = {
             "address": "string",
             "companyName": "string",
             "defaultContact": True,
             "email": "youxiang@163.com",
             "name": "测试重复邮箱手机号",
             "tel": "17826805813",
             "tenantId": 0
        }

    @allure.story('test_email_repeat')
    def test_email_repeat(self):
        path = '/web/tenant-contacts/check'

        data = {
            "address": "string",
            "companyName": "string",
            "defaultContact": True,
            "email": "youxiang@163.com",
            "name": "测试重复邮箱手机号",
            "tel": "17826805889",
            "tenantId": 0
        }

        res = requests.post(a.BASE_URL+path, json=data, headers=self.header)

        res_data = json.loads(res.text)

        assert res_data['emailRepeat'] is True

    @allure.story('test_tel_repeat')
    def test_tel_repeat(self):
        path = '/web/tenant-contacts/check'

        data = {
            "address": "string",
            "companyName": "string",
            "defaultContact": True,
            "email": "youxiang@183.com",
            "name": "测试重复邮箱手机号",
            "tel": "17826805813",
            "tenantId": 0
        }

        res = requests.post(a.BASE_URL + path, json=data, headers=self.header)

        res_data = json.loads(res.text)

        assert res_data['telRepeat'] is True

    @allure.story('test_email_and_tel_repeat')
    def test_all_repeat(self):
        path = '/web/tenant-contacts/check'

        res = requests.post(a.BASE_URL + path, json=self.DATA, headers=self.header)

        res_data = json.loads(res.text)

        assert res_data['emailRepeat'] is True
        assert res_data['telRepeat'] is True

