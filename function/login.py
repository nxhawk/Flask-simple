import json
import os

file1 = os.path.dirname(os.path.abspath(__file__)).replace(
    __file__, '').replace('function', '') + 'database\\isLogin.json'


def _login(usr, psw):
    file = os.path.dirname(os.path.abspath(__file__)).replace(
        __file__, '').replace('function', '') + 'database\\account.json'

    with open(file, 'r') as f:
        data_list = json.load(f)
        if(usr in data_list['usr']):
            index = data_list['usr'].index(usr)
            if(psw != data_list['psw'][index]):
                return False
            else:
                with open(file1, 'r+') as f1:
                    data = json.load(f1)
                    if usr in data['usr']:
                        pass
                    else:
                        data['usr'].append(usr)
                        f1.seek(0)
                        json.dump(data, f1, indent=4)
                return True
        else:
            return False


def _logout():
    with open(file1, 'rb') as fk:
        data = json.load(fk)
        data['usr'].pop(-1)
        open(file1, "w").write(json.dumps(data, indent=4))
