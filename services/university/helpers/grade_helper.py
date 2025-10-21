import requests
from services.general.helpers.base_helper import BaseHelper

class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    def get_stats(self, token: str = None) -> requests.Response:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return self.api_utils.get(f"{self.ENDPOINT_PREFIX}/stats/", headers=headers)

    def post_grade(self, json: dict, token: str = None) -> requests.Response:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return self.api_utils.post(f"{self.ENDPOINT_PREFIX}/", data=json, headers=headers)