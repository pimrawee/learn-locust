from locust import HttpUser, task, constant, SequentialTaskSet
from read_data import CsvRead
from config import URL_HTTPBIN


class MyScript(SequentialTaskSet):
    @task
    def place_order(self):
        # Reading test data from the CSV file
        test_data = CsvRead("dataParameterization\\customer-data.csv").read()
        print(test_data)

        # Preparing the data to be sent in the POST request
        data = {
            "custname": test_data['name'],
            "custtel": test_data['phone'],
            "custemail": test_data['email'],
            "size": test_data['size'],
            "topping": test_data['toppings'],
            "delivery": test_data['time'],
            "comments": test_data['instructions']
        }

        # The name of the order will be the customer's name
        name = "Order for " + test_data['name']

        # Sending a POST request to place the order
        with self.client.post("/post", catch_response=True, name=name, data=data) as response:
            # If the response status code is 200 and contains the customer's name, mark the request as successful
            if response.status_code == 200 and test_data['name'] in response.text:
                response.success()
            # If the order processing fails, mark the request as a failure
            else:
                response.failure("Failure in processing the order")


class MyLoadTest(HttpUser):
    host = URL_HTTPBIN
    wait_time = constant(1)
    tasks = [MyScript]
    
# locust -f path/file.py -u 3 -r 1 -t 5s --only-summary --headless