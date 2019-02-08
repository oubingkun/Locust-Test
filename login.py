from __future__ import print_function
from locust import HttpLocust, TaskSet, task
from hashlib import sha1
import time
import httplib
import json

def auth_header():
    return {"Content-type": "application/json"}

class UserBehavior(TaskSet):
    @task(1)
    def login(self):
        self.tokenInfo = None
        headers = auth_header()
        data = json.dumps({"account":"15898151218","password":"ga871218","type":0})
        response = self.client.request(method="POST", url= "https://appapi-pre.zhaocaapp.cn/user/login",
                                       data = data,
                                       headers = headers)
        print("LOGIN RESULT:", response.status_code, response.content)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://appapi-pre.zhaocapp.cn"
    min_wait = 3000
    max_wait = 5000
