from services.general.helpers.base_helper import BaseHelper
import requests


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    def get_stats(
        self, student_id: int = None, teacher_id: int = None, group_id: int = None
    ) -> requests.Response:
        params = {
            key: value
            for key, value in {
                "student_id": student_id,
                "teacher_id": teacher_id,
                "group_id": group_id,
            }.items()
            if value is not None
        }

        return self.api_utils.get(f"{self.ENDPOINT_PREFIX}/stats/", params=params)

    def post_grade(self, json: dict) -> requests.Response:
        return self.api_utils.post(f"{self.ENDPOINT_PREFIX}/", data=json)