import requests
from services.general.helpers.base_helper import BaseHelper

class UserHelper(BaseHelper):
    ENDPOINT_PREFIX = "/users"

    def get_me(self) -> requests.Response:
        return self.api_utils.get(f"{self.ENDPOINT_PREFIX}/me/")