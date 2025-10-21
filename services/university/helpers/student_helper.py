import requests
from services.general.helpers.base_helper import BaseHelper

class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"

    def post_student(self, json: dict, token: str = None) -> requests.Response:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return self.api_utils.post(f"{self.ENDPOINT_PREFIX}/", json=json, headers=headers)

    def get_student_by_id(self, student_id: int, token: str = None) -> requests.Response:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return self.api_utils.get(f"{self.ENDPOINT_PREFIX}/{student_id}/", headers=headers)