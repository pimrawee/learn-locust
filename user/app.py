from locust import User, task, constant
# User is a class that represents a simulated user in Locust
# task is a decorator to mark methods as tasks that the user will perform
# constant is used to set a fixed wait time between tasks


class MyFirstTest(User):
    weight = 2                  
    # weight determines the relative frequency of this user type
    # A higher weight means this user type will be simulated more often than others

    wait_time = constant(1)
    # wait_time sets a fixed delay between the execution of tasks for this user type

    @task
    def launch(self):
        print("Launching the URL")
    
    @task
    def search(self):
        print("Searching")


class MySecondTest(User):
    weight = 2

    @task
    def launch2(self):
        print("Second Test")

    @task
    def search2(self):
        print("Second Search Test")
        