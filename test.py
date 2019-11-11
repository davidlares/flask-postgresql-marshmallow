import unittest
import json

from app import create_app
from config import config
from app import db

class TestAPI(unittest.TestCase):
    # starting tests
    def setUp(self):
        # setting env to instance
        environment = config['test']
        self.app = create_app(environment)
        # setting up client (from context)
        self.client = self.app.test_client()
        # in-out content_type
        self.content_type = 'application/json'
        self.path = 'http://localhost:5000/api/v1/tasks'

    # after all
    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    # first endpoint test case
    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    # second endpoint test case (filtered)
    def test_get_first_task(self):
        new_path =  self.path + '/1'
        response = self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        # checking if data ID is the same as 1
        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']
        self.assertEqual(task_id, 1)

    # returning 404s intentionally
    def test_not_found(self):
        new_path = self.path + '/100'
        response = self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)

    # create test
    def test_create_task(self):
        data = {
            'title': 'title',
            'description': 'description',
            'deadline': '2020-10-10 12:00:00'
        }
        response = self.client.post(path=self.path, data=json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        # data = json.loads(response.data.decode('utf-8'))
        # task_id = data['data']['id']
        # self.assertEqual(task_id, 5)

    def test_update_task(self):
        data = {'title': 'updated title'}
        new_path =  self.path + '/1'
        response = self.client.put(path=self.new_path, data=json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        # data = json.loads(response.data.decode('utf-8'))
        # task_title = data['data']['title']
        # self.assertEqual(task_title, 'updated title')

    def test_delete_task(self):
        new_path = self.path + '/1'
        response = self.client.delete(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        # you can perform a get in order to hopefully get a 404 response.

if __name__ == "__main__":
    unittest.main()
