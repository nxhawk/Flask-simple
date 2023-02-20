import json
import os


def newAcc(usr, psw):
    file = os.path.dirname(os.path.abspath(__file__)).replace(
        __file__, '').replace('function', '') + 'database\\account.json'
    with open(file, 'r+') as f:
        data_list = json.load(f)
        if usr in data_list['usr']:
            return False
        data_list['usr'].append(usr)
        data_list['psw'].append(psw)
        f.seek(0)
        json.dump(data_list, f, indent=4)
    return True
