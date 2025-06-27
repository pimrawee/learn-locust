from locust import User, task, constant


class MyTest(User):
    wait_time = constant(1)

    def on_start(self):
        print("Starting")
    # This method is called when a simulated user starts executing tasks.
    # It can be used to perform setup actions, such as logging in or initializing data.
    
    @task
    def my_task(self):
        print("My task")

    def on_stop(self):
        print("Stopping")
    # This method is called when a simulated user stops executing tasks.
    # It can be used to perform cleanup actions, such as logging out or releasing resources.


# locust -f .\commandLine\simple_test.py -u 1 -r 1 -t 10s --headless --only-summary
# --only-summary: This option will only print a summary of the test results to the console, without detailed statistics.
