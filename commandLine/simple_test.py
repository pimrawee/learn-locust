from locust import HttpUser, task, constant


class MyLoadTest(HttpUser):
    wait_time = constant(1)  # Wait for 1 second between tasks

    @task
    def launch(self):
        self.client.get("/") # Simulate a GET request to the root URL


# Command run script: locust -f .\commandLine\simple_test.py -u 1 -r 1 -t 10s --headless --print-stats --csv Run1.csv --csv-full-history --host=https://example.com
# The command above runs the test with 1 user, ramping up at a rate of 1 user per second, for a total duration of 10 seconds.
# The results will be printed to the console and saved in a CSV file named Run1.csv
# -u: Number of users to simulate
# -r: Rate at which users are spawned (users per second)
# -t: Total time to run the test
# --headless: Run in headless mode (no web interface)
# --print-stats: Print statistics to the console
# --csv: Save results in CSV format
# --csv-full-history: Save full history of requests in CSV format
# --host: The target host for the load test (replace with your target URL)
