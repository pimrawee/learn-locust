from locust import HttpUser, SequentialTaskSet, task, constant
import re
import random
from config import URL_PET  # URL=https://petstore.octoperf.com


class PetStore(SequentialTaskSet):
    def __init__(self, parent):
        super().__init__(parent)    # Initializing the parent class
        self.jsession = ""          # Session ID placeholder
        self.random_product = ""    # Random product ID placeholder

    @task
    def home_page(self):
        with self.client.get("", catch_response=True, name="T00_HomePage") as response:
            if "Welcome to JPetStore 6" in response.text and response.elapsed.total_seconds() < 2.0:    # If the page is loaded correctly and quickly, mark it as successful
                response.success()
            else:
                response.failure("Home page took too long to load and/or text check has failed.")       # Otherwise, mark the request as failed

    @task
    def enter_store(self):
        products = ['Fish', 'Dogs', 'Cats', 'Reptiles', 'Birds']
        with self.client.get("/actions/Catalog.action", catch_response=True, name="T10_EnterStore") as response:
            for product in products:    # Check if each product is present on the page
                if product in response.text:    
                    response.success()
                else:
                    response.failure("Products check failed.")
                    break
            try:
                jsession = re.search(r"jsessionid=(.+?)\?", response.text)  # Extracting the jsession id from the response to maintain session
                self.jsession = jsession.group(1)
            except AttributeError:
                self.jsession = ""  # Handle missing jsession

    @task
    def signin_page(self):
        self.client.cookies.clear()     # Clear cookies to simulate a fresh session
        url = "/actions/Account.action;jsessionid=" + self.jsession + "?signonForm="    # Construct the sign-in URL using the jsession ID
        with self.client.get(url, catch_response=True, name="T20_SignInPage") as response:
            if "Please enter your username and password." in response.text:
                response.success()
            else:
                response.failure("Sign in page check failed")

    @task
    def login(self):
        self.client.cookies.clear()         # Clear cookies to simulate a fresh session
        url = "/actions/Account.action"
        data = {
            "username": "j2ee", # Hardcoded username
            "password": "j2ee", # Hardcoded password
            "signon": "Login"   # Action to perform on the form
        }
        with self.client.post(url, name="T30_SignIn", data=data, catch_response=True) as response:
            # print(response.text)
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    random_product = re.findall(r"Catalog.action\?viewCategory=&categoryId=(.+?)\"", response.text)  # Extract a list of all product categories from the response
                    self.random_product = random.choice(random_product)  # Storing the random product
                except AttributeError:
                    self.random_product = ""    # Handle missing product ID
            else:
                response.failure("Sign in Failed")

    @task
    def random_product_page(self):
        url = "/actions/Catalog.action?viewCategory=&categoryId=" + self.random_product     # Navigate to a random product page using the selected product ID
        name = "T40_" + self.random_product + "_Page"
        with self.client.get(url, name=name, catch_response=True) as response:
            if self.random_product in response.text:
                response.success()
            else:
                response.failure("Product page not loaded")

    @task
    def sign_out(self):
        with self.client.get("/actions/Account.action?signoff=", name="T50_SignOff", catch_response=True) as response:  # Simulate logging out from the account
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Log off failed")
        self.client.cookies.clear()     # Clear cookies after sign-off


class LoadTest(HttpUser):
    host = URL_PET
    wait_time = constant(1)
    tasks = [PetStore]


# locust -f path/file.py -u 1 -r 1 -t 20s --headless --only-summary