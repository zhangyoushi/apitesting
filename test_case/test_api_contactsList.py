import json
import requests
import unittest
import config.settings as a
import common.Login
import common.Common
import allure


@allure.feature('test_ContactList')
class TestTenantContactCheck(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.token = common.Login.login()
        common.Common.creat_tenant(cls.token, '测试重复邮箱手机号')

        cls.header = {
            'Authorization': cls.token,
            'content-type': 'application/json; charset=utf-8'
        }

        cls.target = {
            "address": "string",
            "companyName": "string",
            "defaultContact": True,
            "email": "youxiang@163.com",
            "name": "测试重复邮箱手机号",
            "tel": "17826805813",
            "tenantId": None,
            'id': 87943
        }

    # 通过姓名搜索联系人
    @allure.story('test_search_by_name')
    def test_search_by_name(self):

        path = '/web/tenant-contacts'
        param = {
            'keyword': '测试重复邮箱手机号'
        }

        t_data = requests.get(a.BASE_URL + path, params=param, headers=self.header)

        t_dict = json.loads(t_data.text)

        assert self.target in t_dict['items']

    # 通过电话号码搜索联系人
    @allure.story('test_search_by_tel')
    def test_search_by_tel(self):

        path = '/web/tenant-contacts'
        param = {
            'keyword': '1782680'
        }

        t_data = requests.get(a.BASE_URL + path, params=param, headers=self.header)

        t_dict = json.loads(t_data.text)

        self.assertIn(self.target, t_dict['items'])

    # 通过公司搜索联系人
    @allure.story('test_search_by_companyName')
    def test_search_by_companyName(self):

        path = '/web/tenant-contacts'
        param = {
            'keyword': 'str'
        }

        t_data = requests.get(a.BASE_URL + path, params=param, headers=self.header)

        t_dict = json.loads(t_data.text)

        self.assertIn(self.target, t_dict['items'])

    # 通过公司筛选
    @allure.story('test_screen_by_companyName')
    def test_screen_by_companyName(self):

        path = '/web/tenant-contacts'
        param = {
            'companies': 'string'
        }

        t_data = requests.get(a.BASE_URL + path, params=param, headers=self.header)

        t_dict = json.loads(t_data.text)

        self.assertIn(self.target, t_dict['items'])

    # 通过是否默认联系人筛选
    @allure.story('test_screen_by_default')
    def test_screen_by_default(self):

        path = '/web/tenant-contacts'
        param = {
            'defaultContact': True
        }

        t_data = requests.get(a.BASE_URL + path, params=param, headers=self.header)

        t_dict = json.loads(t_data.text)

        self.assertIn(self.target, t_dict['items'])
