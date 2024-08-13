from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def user_create(self):
        payload = {
            "id": 112233,
            "username": "didi",
            "firstName": "dilek",
            "lastName": "dilek",
            "email": "didi@mail.com",
            "password": "123456",
            "phone": "555666",
            "userStatus": 0
        }
        self.client.post("v2/user", json=payload)

    @task
    def user_login(self):
        self.client.get()