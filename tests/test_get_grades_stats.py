import requests
from services.university.helpers.grade_helper import GradeHelper


class TestGradesStats:
    def test_get_grades_stats(self, university_api_utils_admin):
        grade_helper = GradeHelper(api_utils=university_api_utils_admin)

        response = grade_helper.get_stats()

        assert response.status_code == requests.status_codes.codes.ok, (
            f"Expected 200, got {response.status_code}"
        )

        stats = response.json()
        assert all(key in stats for key in ("avg", "min", "max")), "Missing keys in stats response"