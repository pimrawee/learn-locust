from locust import HttpUser, task, constant, SequentialTaskSet, events
import logging


@events.spawning_complete.add_listener
# Setting up the event listener for the spawning_complete event
# This event will be triggered when users (virtual users) are spawned
def spawn_users(user_count, **kwargs):
    print("Spawned ... ", user_count, " users.")


@events.request.add_listener
# Setting up the event listener for the all request event
# This event will be triggered after every request (success or failure)
def handle_request(**kwargs):
    exception = kwargs.get("exception")
    response = kwargs.get("response")
    # Check if the request was successful:
    # - No exception occurred
    # - Response is not None
    # - HTTP status code is less than 400 (i.e., not an error)
    if exception is None and response is not None and response.status_code < 400:
        print("Sending the success notification")
    else:
        print("Sending the failed notification")


@events.quitting.add_listener
# Setting up the event listener for the quitting event
# This event will be triggered when the test finishes or quits
def sla(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:                   # Check the failure ratio after the test completes
        logging.error("Test failed due to failure ratio > 0.01%")   # If the failure ratio is greater than 0.01, log an error message
        environment.process_exit_code = 1                           # Set the exit code to 1 to indicate a test failure
        print(environment.process_exit_code)
    else:
        environment.process_exit_code = 0                           # If the failure ratio is within the acceptable limit, set the exit code to 0
        print(environment.process_exit_code)


class LoadTest(SequentialTaskSet):
    @task
    def home_page(self):
        self.client.get("/", name="T00_SuccessRequests")        # Send a GET request to the home page
        self.client.get("/failed", name="T01_FailRequests")     # Send a GET request to a non-existent page to simulate a failure


class TestScenario(HttpUser):
    wait_time = constant(1)
    tasks = [LoadTest]


# locust -f path/file.py --config locust.conf