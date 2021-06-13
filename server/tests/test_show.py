import unittest
import requests
import os
from utils import get_token
import logging


class read_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.headers = {'token': get_token()}
        cls.url = 'http://127.0.0.1/file'

    def test_smoke(self):
        path = os.path.abspath(os.path.dirname(__file__))
        r = requests.get(self.url+path, headers=self.headers)
        self.assertEqual(True, isinstance(r.json()['list'], list),msg=r.json())

    def test_not_exist_dir(self):
        path = os.path.abspath(os.path.dirname(__file__)) + "1"
        r = requests.get(self.url+path, headers=self.headers)
        self.assertIn('目录不存在', r.json()['msg'], msg=path)

    def test_login_access(self):
        path = os.path.abspath(os.path.dirname(__file__)) + "1"
        r = requests.get(self.url+path)
        self.assertEqual(2, r.json()['code'])
