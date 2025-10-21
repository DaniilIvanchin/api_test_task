import pytest
import requests
from services.university.helpers.student_helper import StudentHelper


class TestStudentNotFound:
    def test_get_student_not_found(self, university_api_utils_admin):
        student_helper = StudentHelper(api_utils=university_api_utils_admin)

        fake_id = 99999
        response = student_helper.get_student_by_id(fake_id)

        assert response.status_code == requests.status_codes.codes.not_found, (
            f"Expected 404 for non-existent student, got {response.status_code}"
        )