import unittest
import json

from app import db
from app import create_app

from config import config

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
        self.path = 'http://127.0.0.1:5000/api/v1/tasks'
        self.path_first_task = self.path + '/1'
        self.path_fake_task = self.path + '/100'
        self.data = {'title': 'title','description': 'description','deadline': '2020-10-10 12:00:00'}
        self.updated_data = {'title': 'updated title'}

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    # first endpoint test case
    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    def get_task_id(self,response):
        data = json.loads(response.data.decode('utf-8'))
        return data['data']['id']

    # second endpoint test case (filtered)
    def test_get_first_task(self):
        response = self.client.get(path=self.path_first_task,content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        # checking if data ID is the same as 1
        task_id = self.get_task_id(response)
        self.assertEqual(task_id, 1)

    # returning 404s intentionally
    def test_not_found(self):
        response = self.client.get(path=self.path_fake_task, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)

    # create test
    def test_create_task(self):
        response = self.client.post(path=self.path, data=json.dumps(self.data),content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        task_id = self.get_task_id(response)
        self.assertEqual(task_id, 3)

    def test_update_task(self):
        response = self.client.put(path=self.path_first_task, data=json.dumps(self.updated_data), content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        title = data['data']['title']
        self.assertEqual(title, self.updated_data['title'])

    def test_delete_task(self):
        response = self.client.delete(path=self.path_first_task, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
        # you can perform a get in order to hopefully get a 404 response.
        response = self.client.get(path=self.path_first_task, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
