from locust import User, task, constant, between, constant_pacing
import time


class Constant(User):
    wait_time = constant(1)  # Wait for 1 second between tasks

    @task
    def launch(self):
        print("This will inject 1 second delay.")


class Between(User):
    wait_time = between(1, 3)  # Wait between 1 and 3 seconds between tasks

    @task
    def launch(self):
        print("This will inject 1-3 seconds delay.")


class ConstantPacing(User):
    wait_time = constant_pacing(3)  
    # Wait for 3 seconds between tasks, but not affected by task execution time
    # This means that even if a task takes longer than 3 seconds, the next task will still start 3 seconds after the previous one finishes.

    @task
    def launch(self):
        time.sleep(5)  
        # Simulate a task that takes 5 seconds
        # This will not affect the pacing, which will still be 3 seconds
        # So the next task will start 3 seconds after this one finishes
        print("Constant Pacing")
