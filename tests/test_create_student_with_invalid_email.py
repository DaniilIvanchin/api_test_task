import random
import requests
from faker import Faker
from services.university.helpers.student_helper import StudentHelper
from services.university.models.enums import DegreeEnum
from services.university.helpers.group_helper import GroupHelper
from services.university.models.group_request import GroupRequest
faker = Faker()


class TestStudentInvalidEmail:
    def test_create_student_with_invalid_email(self, university_api_utils_admin):
        student_helper = StudentHelper(api_utils=university_api_utils_admin)
        group_helper = GroupHelper(api_utils=university_api_utils_admin)

        group_response = group_helper.post_group(
            json=GroupRequest(name=faker.word()).model_dump()
        )
        assert group_response.status_code == requests.codes.created, (
            f"Expected 201, got {group_response.status_code}"
        )
        group_id = group_response.json()["id"]

        invalid_student = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": "not-an-email",
            "degree": random.choice(list(DegreeEnum)).value,
            "phone": faker.numerify("+7##########"),
            "group_id": group_id,
        }

        response = student_helper.post_student(json=invalid_student)

        assert response.status_code == requests.status_codes.codes.unprocessable_entity, (
            f"Expected 422 for invalid email, got {response.status_code}"
        )