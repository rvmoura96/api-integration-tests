from random import choice, randint
from string import ascii_letters

from locust import task
from locust.contrib.fasthttp import FastHttpUser


class SimpleUser(FastHttpUser):
    @task
    def expected_valid_values(self):
        random_int = randint(-10000, 10000)
        self.client.get(f"http://challengeqa.staging.devmuch.io/{random_int}")

    @task
    def expected_negative_invalid_values(self):
        random_int = randint(-20000, -10001)
        self.client.get(f"http://challengeqa.staging.devmuch.io/{random_int}")

    @task
    def expected_positive_invalid_values(self):
        random_int = randint(10001, 20000)
        self.client.get(f"http://challengeqa.staging.devmuch.io/{random_int}")

    @task
    def unexpected_str_values(self):
        random_str = str().join(choice(ascii_letters) for letter in range(10))
        self.client.get(f"http://challengeqa.staging.devmuch.io/{random_str}")
