import json
import os


def isLogin(usr):
    file = os.path.dirname(os.path.abspath(__file__)).replace(
        __file__, '').replace('function', '') + 'database\\isLogin.json'

    with open(file, 'r') as f:
        data_list = json.load(f)
        if usr in data_list['usr']:
            return True
        return False
