import json
from time import sleep

import requests
import unittest
import config.settings as a
import common.Login
from common.Common import *


class TestTenantContact(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.token = common.Login.login()

        cls.header = {
            'Authorization': cls.token,
            'content-type': 'application/json; charset=utf-8'
        }

    def test_delete_1(self):
        # 创建删除的租客
        t_id = check_tenant(self.token, '测试删除联系人')

        if not t_id:
            creat_tenant(self.token, '测试删除联系人')
            t_id = check_tenant(self.token, '测试删除联系人')

        path = '/web/tenant-contacts/'

        requests.delete(a.BASE_URL+path+str(t_id[0]), headers=self.header)

        t_status = check_tenant(self.token, '测试删除联系人')
        assert len(t_status) == 0

    def test_batch_delete(self):

        path = '/web/tenant-contacts/'
        # 创建删除的租客

        t_id = check_tenant(self.token, '测试删除联系人')

        if not t_id:
            creat_tenant(self.token, '测试删除联系人', num=3)
            t_id = check_tenant(self.token, '测试删除联系人')

        for i in range(len(t_id)):
            path = path + t_id[i]+','

        res = requests.delete(a.BASE_URL+path.strip(','), headers=self.header)

        t_status = check_tenant(self.token, '测试删除联系人')
        assert len(t_status) == 0
        sleep(1)
