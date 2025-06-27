from locust import SequentialTaskSet, HttpUser, constant, task
from config import URL_CAT


# SequentialTaskSet allows you to define a sequence of tasks that will be executed in order
# Each task will be executed one after the other, and you can control the flow of execution
class MySequentialTaskSet(SequentialTaskSet):
    @task
    def get_status(self):
        self.client.get("/200")
        print("Status of 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Status of 500")

    
class MyUser(HttpUser):
    host = URL_CAT   # URL_CAT=https://http.cat/
    tasks = [MySequentialTaskSet]
    wait_time = constant(1)