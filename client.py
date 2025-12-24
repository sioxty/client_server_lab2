import requests
from typing import List
import logging

logging.basicConfig(level=logging.INFO)

BASE_URL = "https://meowfacts.herokuapp.com/"


class ApiClient:
    def __init__(self, timeout: int = 10):
        self.session = requests.Session()
        self.timeout = timeout
        self.session.headers.update({
            "Accept": "application/json"
        })

    def get_facts(self, count: int = 1) -> List[str]:
        response = self.session.get(
            BASE_URL,
            params={"count": count},
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json().get("data", [])
