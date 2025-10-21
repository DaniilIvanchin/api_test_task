import json
import requests
from requests import Session
from utils.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)

        print(f"\nRequest: {response.request.method} {response.request.url}")
        if response.request.body:
            print("Request body:", response.request.body)

        if JsonUtils.is_json(response.text):
            body = json.dumps(response.json(), indent=2, ensure_ascii=False)
        else:
            body = response.text

        print(f"\nResponse status code: {response.status_code}")
        print(f"Response time: {response.elapsed.total_seconds()}s")
        print(f"Response body:\n{body}\n")

        return response
    return _log_response


class ApiUtils:

    def __init__(self, url: str, headers: dict = None):
        self.session = Session()
        self.url = url
        self.session.headers.update(headers or {})

    @log_response
    def get(self, endpoint_url: str, **kwargs):
        return self.session.get(self.url + endpoint_url, **kwargs)

    @log_response
    def post(self, endpoint_url: str, data=None, json=None, **kwargs):
        return self.session.post(self.url + endpoint_url, data=data, json=json, **kwargs)