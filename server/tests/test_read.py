import unittest
import requests
import os
from utils import get_token
import logging


class read_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.headers = {'token': get_token()}
        cls.url = 'http://127.0.0.1/read'

    def test_smoke(self):
        data = {'path': os.path.abspath(__file__)}
        r = requests.post(self.url, data=data, headers=self.headers)
        self.assertIn('read_case', r.json()['text'])

    def test_not_exist_file(self):
        data = {'path': os.path.abspath(__file__)+'1'}
        r = requests.post(self.url, data=data, headers=self.headers)
        self.assertIn('文件不存在', r.json()['msg'],msg=data['path'])

    def test_login_access(self):
        data = {'path': os.path.abspath(__file__)}
        r = requests.post(self.url, data=data)
        self.assertEqual(2,r.json()['code'])