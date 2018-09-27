# @uthor: Diego Narducci Arioza

import requests
import json
import sys

class Zbx_azws_addons(object):


    def __init__(self, url, login="Admin", password="zabbix"):
        self.headers = {'content-type': 'application/json'}
        self.url = url + '/api_jsonrpc.php'
        self.login = login
        self.password = password

    def login_auth(self):
        self.datapl = {'jsonrpc': '2.0', 'method': 'user.login', 'params': {'user': self.login, 'password': self.password}, 'id': '1'}
        req = requests.post(self.url, data=json.dumps(self.datapl), headers=self.headers, verify=False)
        return req.json()['result']

    def cadastrar_Host(self):
        cadastro = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": "teste_5",
                "interfaces": [{
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": "1.2.3.4",
                    "dns": "",
                    "port": "10050"
                }],
                "groups": [{
                    "groupid": 15
                }]
            },
            "auth": self.login_auth(),
            "id": 1
        }

        req = requests.post(self.url, data=json.dumps(cadastro), headers=self.headers, verify=False)
        if 'error' not in req.json():
            print("Host com id \"{}\" adicionado com sucesso".format(req.json()['result']['hostids'][0]))
        else:
            print("Deu Merda - \"{}\"".format(req.json()['error']['data']))


host1 = Zbx_azws_addons("https://zabbix.azws.com.br", "telegram", "telegram")

host1.cadastrar_Host()