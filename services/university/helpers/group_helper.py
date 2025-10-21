import requests
from services.general.helpers.base_helper import BaseHelper

class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups"

    def post_group(self, json: dict, token: str = None) -> requests.Response:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return self.api_utils.post(f"{self.ENDPOINT_PREFIX}/", json=json, headers=headers)

    def get_groups(self, token: str = None) -> requests.Response:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return self.api_utils.get(f"{self.ENDPOINT_PREFIX}/", headers=headers)