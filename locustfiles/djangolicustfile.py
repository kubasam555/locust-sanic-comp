import json

from locust import HttpLocust, TaskSet, task


class PostBehavior(TaskSet):

    def on_start(self):
        # self.headers = {'Authorization': 'Token 4dd73681a4d464c5bf64599da2c2ea554327c329'}
        self.headers = {'content-type': 'application/json'}
        self.client.headers = self.headers

    def on_stop(self):
        self.client.headers = []

    @task(1)
    def posts(self):
        self.client.get('post/')

    @task(1)
    def post(self):
        self.client.get('post/1/')

    @task(2)
    def login(self):
        data = {
            'username': 'user',
            'password': 'user1234'
        }
        self.client.post('auth/login', json.dumps(data))


class WebsitePost(HttpLocust):
    task_set = PostBehavior
    min_wait = 5000
    max_wait = 9000
