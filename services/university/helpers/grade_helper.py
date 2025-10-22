from services.general.helpers.base_helper import BaseHelper
import requests


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    def get_stats(
            self, student_id: int = None, teacher_id: int = None, group_id: int = None
    ) -> requests.Response:
        url = f"{self.ENDPOINT_PREFIX}/stats/"

        query_params = []
        if student_id:
            query_params.append(f"student_id={student_id}")
        if teacher_id:
            query_params.append(f"teacher_id={teacher_id}")
        if group_id:
            query_params.append(f"group_id={group_id}")

        if query_params:
            url += "?" + "&".join(query_params)

        return self.api_utils.get(url)

    def post_grade(self, json: dict) -> requests.Response:
        return self.api_utils.post(f"{self.ENDPOINT_PREFIX}/", data=json)