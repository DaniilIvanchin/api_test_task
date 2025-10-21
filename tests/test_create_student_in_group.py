from services.university.university_service import UniversityService
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from faker import Faker
from services.university.models.enums import DegreeEnum
import random

fake = Faker()

def test_create_student(university_api_utils_admin):
    university_service = UniversityService(university_api_utils_admin)

    group_request = GroupRequest(name=fake.word())
    group_response = university_service.create_group(group_request)

    student_request = StudentRequest(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        degree=random.choice(list(DegreeEnum)).value,
        phone=fake.numerify("+7##########"),
        group_id=group_response.id
    )

    student_response = university_service.create_student(student_request)

    assert student_response.group_id == group_response.id, (
        f"Wrong group ID: expected {group_response.id}, got {student_response.group_id}"
    )