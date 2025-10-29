import requests
from services.general.helpers.base_helper import BaseHelper

class TeacherHelper(BaseHelper):
    ENDPOINT_PREFIX = "/teachers"

    def post_teacher(self, json: dict) -> requests.Response:
        return self.api_utils.post(f"{self.ENDPOINT_PREFIX}/", json=json)