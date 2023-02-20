import json
import unittest

from main import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_1(self):
        response = self.client.get('/')
        assert response.data == b'Hello guy'

    def test_2(self):
        response = self.client.get('/sum/100/200')
        assert response.data == b'The sum of 100 and 200 is: 300'

    def test_3(self):
        response = self.client.post(
            '/login', data=json.dumps({'name': 'Nhat Hao', 'age': 20}), content_type='application/json')
        print(response.data)
        assert response.data == b'Hello Nhat Hao, age 20'
