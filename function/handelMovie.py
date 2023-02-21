import json
import os

file = os.path.dirname(os.path.abspath(__file__)).replace(
    __file__, '').replace('function', '') + 'database\\movies.json'


def _getAllMovie():
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data = data['movies']
        return data


def _addMovie(data):
    with open(file, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        data_list['movies'].insert(0, {"name": data['name'], "rate": data['rate'],
                                       "year": data['year'], "userAdd": data['user'], "editBy": data['user']})
        open(file, "w", encoding='utf-8').write(json.dumps(data_list,
                                                           indent=4, ensure_ascii=False))


def _delMovie(data):
    with open(file, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        data_list['movies'].pop(int(data['stt']))
        open(file, "w", encoding='utf-8').write(json.dumps(data_list,
                                                           indent=4, ensure_ascii=False))


def _editMovie(data):
    with open(file, 'r', encoding='utf-8') as f:
        data_list = json.load(f)
        user = data_list['movies'][int(data['stt'])]['userAdd']
        data_list['movies'][int(data['stt'])] = {"name": data['name'], "rate": data['rate'],
                                                 "year": data['year'], "userAdd": user, "editBy": data['user']}
        open(file, "w", encoding='utf-8').write(json.dumps(data_list,
                                                           indent=4, ensure_ascii=False))
