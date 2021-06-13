import unittest
import requests


class login_case(unittest.TestCase):
    def test_error_username(self):
        username = '1'
        data = {"username": username, 'password': 'raspberry'}
        r = requests.post('http://127.0.0.1/login', data=data)
        self.assertEqual(r.json()['msg'], '不存在该用户')

    def test_error_password(self):
        password = '1'
        data = {"username": 'pi', 'password': password}
        r = requests.post('http://127.0.0.1/login', data=data)
        self.assertEqual(r.json()['msg'], '密码错误')

    def test_smoke(self):
        data = {"username": 'pi', 'password': 'raspberry'}
        r = requests.post('http://127.0.0.1/login', data=data)
        self.assertIn('token', r.json().keys())