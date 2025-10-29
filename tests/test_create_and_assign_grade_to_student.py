import random
from faker import Faker
import requests
from services.university.university_service import UniversityService
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.grade_request import GradeRequest
from services.university.models.enums import DegreeEnum, SubjectEnum
from services.university.models.grade_constants import MAX_GRADE, MIN_GRADE

faker = Faker()


class TestCreateAndAssignGrade:
    def test_create_and_assign_grade_to_student(self, university_api_utils_admin):
        university_service = UniversityService(university_api_utils_admin)

        group = university_service.create_group(GroupRequest(name=faker.word()))
        student = university_service.create_student(
            StudentRequest(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                degree=random.choice(list(DegreeEnum)).value,
                phone=faker.numerify("+7##########"),
                group_id=group.id
            )
        )
        teacher_response = university_service.teacher_helper.post_teacher(
            json=TeacherRequest(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                subject=random.choice(list(SubjectEnum)).value
            ).model_dump()
        )

        teacher = teacher_response.json()

        grade_response = university_service.grade_helper.post_grade(
            json=GradeRequest(
                teacher_id=teacher["id"],
                student_id=student.id,
                grade=random.randint(MIN_GRADE, MAX_GRADE)
            ).model_dump()
        )

        assert grade_response.status_code == requests.status_codes.codes.created, (
            f"Wrong status code. Actual: {grade_response.status_code}, "
            f"expected: {requests.status_codes.codes.created}"
        )