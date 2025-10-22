import json
import curlify
import requests
from requests import Session
from logger.logger import Logger
from utils.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)

        Logger.info(f"Request: {curlify.to_curl(response.request)}")

        body = (
            json.dumps(response.json(), indent=2, ensure_ascii=False)
            if JsonUtils.is_json(response.text)
            else response.text
        )

        Logger.info(
            f"Response status code={response.status_code}, "
            f"elapsed_time={response.elapsed.total_seconds()}s\n{body}\n"
        )

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