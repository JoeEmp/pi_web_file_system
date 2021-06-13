import unittest
import requests
import os
from utils import get_token
import logging


class read_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.headers = {'token': get_token()}
        cls.url = 'http://127.0.0.1/edit'

    def test_smoke(self):
        data = {'path': os.path.abspath(os.path.dirname(__file__))+'/for_joe.txt','text':'smoke_test'}
        r = requests.post(self.url, data=data, headers=self.headers)
        self.assertEqual(0, r.json()['code'])

    def test_edit_not_exist_file(self):
        data = {'path': os.path.abspath(os.path.dirname(__file__))+'/for_joe.txt1','text':'smoke_test'}
        r = requests.post(self.url, data=data, headers=self.headers)
        self.assertIn('文件不存在', r.json()['msg'],msg=data['path'])

    def test_login_access(self):
        data = {'path': os.path.abspath(__file__)}
        r = requests.post(self.url, data=data)
        self.assertEqual(2,r.json()['code'])