import json
import requests
import config.settings as a


def login():

    path = '/oauth/token/password'

    data = {'client_id': a.CLIENT_ID, 'username': a.USERNAME, 'password': a.PASSWORD}

    res = requests.post(a.BASE_URL+path, data=data)

    data = json.loads(res.text)

    return 'Bearer ' + data['access_token']