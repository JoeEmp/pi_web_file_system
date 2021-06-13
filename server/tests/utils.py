import requests
import jwt
import time


def sync_token(token):
    return jwt.decode(token, verify=False, algorithms=['HS256'])


def is_exp(token):
    token_info = sync_token(token)
    return True if token_info['exp'] <= time.time() else False


def get_token():
    try:
        with open('token.txt') as f:
            token = f.read()
            if not token:
                raise ValueError('token为空')
            if is_exp(token):
                raise ValueError('token已过期')
            return token
    except Exception as e:
        data = {'username': 'pi', 'password': 'raspberry'}
        token = requests.post('http://127.0.0.1/login',
                              data=data).json()['token']
        with open('token.txt', 'w') as f:
            f.write(token)
        return token


get_token()
