import pytest
import requests
from faker import Faker
from services.university.helpers.student_helper import StudentHelper

faker = Faker()


class TestStudentInvalidEmail:
    def test_create_student_with_invalid_email(self, university_api_utils_admin):
        student_helper = StudentHelper(api_utils=university_api_utils_admin)

        invalid_student = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": "not-an-email",
            "degree": "Bachelor",
            "phone": "+78005553535",
            "group_id": 1
        }

        response = student_helper.post_student(json=invalid_student)

        assert response.status_code == requests.status_codes.codes.unprocessable_entity, (
            f"Expected 422 for invalid email, got {response.status_code}"
        )