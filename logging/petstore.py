from locust import HttpUser, SequentialTaskSet, task, constant
from config import URL_PET  # URL=https://petstore.octoperf.com
import logging


class PetStore(SequentialTaskSet):
    @task
    def home_page(self):
        with self.client.get("/", catch_response=True, name="T00_HomePage") as response:
            if "Welcome to JPetStore 6" in response.text and response.elapsed.total_seconds() < 2.0:
                response.success()
                logging.info("Home Page load success")
            else:
                response.failure("Home page took too long to load and/or text check has failed.")
                logging.error("Home page didn't load successfully.")


class LoadTest(HttpUser):
    host = URL_PET
    wait_time = constant(1)
    tasks = [PetStore]


# How to use Logging in Locust:
#   • Importing the Logging Module: You need to import the logging module to use it.
#   • Logging Information: You can log information using various logging functions, such as:
#     ◦ logging.info(): For general information.
#     ◦ logging.error(): For logging errors.
#     ◦ logging.critical(): For logging critical errors.
#     ◦ logging.debug(): For detailed debugging information.
#     ◦ logging.warning(): For logging warnings.
# Command Line Options for Logging Configuration:
#   • skip log setup: Used to skip the default log setup.
#   • log file [filename]: Used to log information to a specified file. For example, if you specify "mylog.log", all logs will be saved in that file.
#   • Adjusting the Logging Level: By default, Locust uses the 'info' level. However, if you need more detailed information for debugging, you can change it to 'debug'. When using 'debug', you will get more detailed logs, which are useful for debugging your scripts.


# Command
# locust -f path/file.py --logfile path/mylog.log --headless --only-summary -u 1 -r 1 -t 10s


# Caution:
# Avoid naming your file as "logging.py" because it conflicts with the built-in "logging" module.
# This will prevent the program from running correctly.
