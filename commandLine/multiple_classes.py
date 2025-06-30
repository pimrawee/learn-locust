from locust import HttpUser, task, constant, TaskSet


class FirefoxBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Firefox Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class ChromeBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Chrome Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class EdgeBrowserTest(TaskSet):
    @task
    def launch(self):
        print("Edge Browser Tests")
        self.client.get("/", name=self.__class__.__name__)
        self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    wait_time = constant(1)
    tasks = [ChromeBrowserTest, FirefoxBrowserTest, EdgeBrowserTest]


# locust -f .\commandLine\multiple_classes.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history --host=https://example.com -L DEBUG --logfile my.log.log --html Run1.html
# The command above runs the test with 1 user, ramping up at a rate of 1 user per second, for a total duration of 10 seconds.
# The results will be printed to the console and saved in a CSV file named Run1.csv
# -L DEBUG: Set the logging level to DEBUG
# --logfile my.log.log: Save the log output to a file named my.log.log
# --html Run1: Generate an HTML report named Run1.html
# --host: The target host for the load test (replace with your target URL)

# locust -f .\commandLine\multiple_classes.py -l
# This command will list all the tasks defined in the script.

# locust -f .\commandLine\multiple_classes.py --show-task-ratio
# This command will list all the tasks defined in the script along with their ratios.
