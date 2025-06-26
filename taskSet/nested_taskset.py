from locust import TaskSet, constant, task, HttpUser
from config import URL_CAT


class MyCat(TaskSet):
    @task
    def get_status(self):
        self.client.get("/200")
        print("GET Status of 200")
        self.interrupt(reschedule=False)
        # self.interrupt() This will stop the current task
        # self.interrupt(reschedule=True) This will stop the current task and reschedule it
        # self.interrupt(reschedule=False) This will stop the current task and not reschedule it


class MyAnotherCat(TaskSet):
    @task
    def get_500_status(self):
        self.client.get("/500")
        print("GET Status of 500")
        self.interrupt(reschedule=False)
        
            
class MyLoadTest(HttpUser):
    host = URL_CAT  # URL_CAT=https://http.cat/
    tasks = [MyCat, MyAnotherCat]
    wait_time = constant(1)
    