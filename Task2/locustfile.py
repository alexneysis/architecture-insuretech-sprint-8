from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_insurances(self):
        self.client.get("/")