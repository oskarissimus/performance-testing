from locust import HttpUser, task


class WebsiteUser(HttpUser):
    host = "http://localhost:8000"
    
    @task
    def instant(self):
        self.client.get("/instant")
    
    @task
    def wait(self):
        self.client.get("/wait")

    @task
    def wait_random(self):
        self.client.get("/wait-random")