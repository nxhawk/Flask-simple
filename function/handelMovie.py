import json
import os

file = os.path.dirname(os.path.abspath(__file__)).replace(
    __file__, '').replace('function', '') + 'database\\movies.json'


def _getAllMovie():
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        data = data['movies']
        return data
