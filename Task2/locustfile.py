from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(0.1, 0.5)  # уменьшим интервал, чтобы быстрее поднять утилизацию памяти

    @task
    def index(self):
        self.client.get("/")