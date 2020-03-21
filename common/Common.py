import json
from time import sleep

import common.Login
import requests
import config.settings as a


def creat_str():
    test = ''
    i = 0

    while i < 21:
        test = test + '一二三四五六七八九十'
        i = i + 1

    return test


def creat_tenant(token, name, num=1):

    param = {
            'keyword': name
    }

    header = {
        'Authorization': token,
        'content-type': 'application/json; charset=utf-8'
    }

    t_data = requests.get(a.BASE_URL+'/web/tenant-contacts', params=param, headers=header)

    t_dict = json.loads(t_data.text)

    # print(t_dict)
    """
    flag = True表示此人存在
    
    """

    if t_dict['items']:
        flag = True
    else:
        flag = False

    # 如果没有此人，则创建租客联系人

    path = '/web/tenant-contacts'

    data = {
        "address": "string",
        "companyName": "string",
        "defaultContact": True,
        "email": "youxiang@163.com",
        "name": name,
        "tel": "17826805813",
        "tenantId": 0
    }

    if not flag:
        try:
            for i in range(num):
                res = requests.post(a.BASE_URL + path, json=data, headers=header)

        except Exception as e:

            print(e)
    else:
        print('该联系人已存在')


def check_tenant(token, name):
    param = {
        'keyword': name
    }

    header = {
        'Authorization': token,
        'content-type': 'application/json; charset=utf-8'
    }

    t_data = requests.get(a.BASE_URL + '/web/tenant-contacts', params=param, headers=header)

    t_dict = json.loads(t_data.text)

    t_id = []
    print(t_dict)

    if t_dict['items']:
        for k in range(len(t_dict['items'])):
            t_id.append(str(t_dict['items'][k]['id']))

    sleep(1)

    return t_id

