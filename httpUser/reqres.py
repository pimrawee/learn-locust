from locust import HttpUser, constant, task
from config import URL, API_KEY


class MyReqRes(HttpUser):
    wait_time = constant(1)
    host = URL  # URL=https://reqres.in


    # Define the headers to be used in all requests
    def on_start(self):
        self.headers = {
            "x-api-key": API_KEY,
        }


    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2", headers=self.headers)
        print("GET:", res.status_code)
        print("GET:", res.text)
        print("GET:", res.headers)

    @task
    def create_user(self):
        res = self.client.post(
            "/api/users",
            json={"name": "morpheus", "job": "leader"},
            headers=self.headers
        )
        print("POST:", res.status_code)

    @task
    def update_user(self):
        res = self.client.put(
            "/api/users/2",
            json={"name": "morpheus", "job": "zion resident"},
            headers=self.headers
        )
        print("PUT:", res.status_code)

    @task
    def delete_user(self):
        res = self.client.delete("/api/users/2", headers=self.headers)
        print("DELETE:", res.status_code)