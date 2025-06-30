from locust import HttpUser, task, constant, SequentialTaskSet
from config import URL_HTTPBIN  # URL="https://httpbin.org"


class MyScript(SequentialTaskSet):
    @task
    def get_xml(self):
        result = self.client.get("/xml", name="XML")
        print(result)   # <Response [200]>

    @task
    def get_json(self):
        expected_response = "Wake up to WonderWidgets!" # 

        with self.client.get("/json", catch_response=True, name="JSON") as response:    # catch_response
            result = True if expected_response in response.text else False      # Pythonic if else statement
            print(self.get_json.__name__, result)   # Prints True if the response contains 'expected_response', else False -> get_json True
            response.success()  # Making thsis as success

    @task
    def get_robots(self):
        expected_response = "*"
        result = "Fail"
        with self.client.get("/robots.txt", catch_response=True, name="Robots") as response:
            if expected_response in response.text:
                result = "Success"
                response.failure("Not a failure")   # Marking this success request intentional failure
        print(self.get_robots.__name__, result)     # get_robots Success

    @task
    def get_failure(self):
        expected_response = 404
        with self.client.get("/status/404", catch_response=True, name="HTTP 404") as response:
            if response.status_code == expected_response:
                response.failure("Got 404!")
            else:
                response.success()
        print(self.get_failure.__name__, response.status_code)     # get_failure 404


class MyLoadTest(HttpUser):
    host = URL_HTTPBIN
    wait_time = constant(1)
    tasks = [MyScript]
