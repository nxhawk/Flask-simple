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
                                       "year": data['year'], "userAdd": data['user']})
        open(file, "w", encoding='utf-8').write(json.dumps(data_list,
                                                           indent=4, ensure_ascii=False))
