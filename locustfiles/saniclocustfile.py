import json

from locust import HttpLocust, TaskSet, task


class PostBehavior(TaskSet):

    def on_start(self):
        # self.headers = {'Authorization': 'Token b2a2d49b022c446c9b783b07873c50ec'}
        self.headers = {'content-type': 'application/json'}
        self.client.headers = self.headers

    def on_stop(self):
        self.client.headers = []

    @task(1)
    def posts(self):
        self.client.get('post')

    @task(2)
    def post(self):
        self.client.get('post/2')

    @task(2)
    def login(self):
        data = {
            "username": "admin1",
            "password": "user1234"
        }
        self.client.post('auth/login/', data=json.dumps(data))


class WebsitePost(HttpLocust):
    task_set = PostBehavior
    min_wait = 5000
    max_wait = 9000
