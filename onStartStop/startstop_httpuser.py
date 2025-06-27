from locust import HttpUser, task, constant, SequentialTaskSet
from config import URL_ONLINE_BOUTIQUE # URL=https://onlineboutique.dev


class MyTest(SequentialTaskSet):
    wait_time = constant(1)

    def on_start(self):
        self.client.get("/", name=self.on_start.__name__)
        print("Start")

    @task
    def browse_product(self):
        self.client.get("/product/OLJCESPC7Z", name=self.browse_product.__name__)
        print("Browse Product")

    @task
    def cart_page(self):
        self.client.get("/cart", name=self.browse_product.__name__)
        print("Cart Page")

    def on_stop(self):
        self.client.get("/", name=self.on_stop.__name__)
        print("Stop")


class LoadTest(HttpUser):
    host = URL_ONLINE_BOUTIQUE
    tasks = [MyTest]
    wait_time = constant(1)