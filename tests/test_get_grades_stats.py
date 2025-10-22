import random
import requests
from faker import Faker
from services.university.university_service import UniversityService
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.grade_request import GradeRequest
from services.university.models.enums import DegreeEnum, SubjectEnum

faker = Faker()
min_grade = 1
max_grade = 5

class TestGradesStats:
    def test_get_grades_stats_with_data(self, university_api_utils_admin):

        university_service = UniversityService(university_api_utils_admin)

        group = university_service.create_group(GroupRequest(name=faker.word()))
        student = university_service.create_student(
            StudentRequest(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                degree=random.choice(list(DegreeEnum)).value,
                phone=faker.numerify("+7##########"),
                group_id=group.id,
            )
        )

        teacher = university_service.create_teacher(
            TeacherRequest(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                subject=random.choice(list(SubjectEnum)).value,
            )
        )

        grades = [random.randint(min_grade, max_grade) for _ in range(5)]
        for g in grades:
            university_service.create_grade(
                GradeRequest(
                    teacher_id=teacher.id,
                    student_id=student.id,
                    grade=g,
                )
            )

        stats_response = university_service.grade_helper.get_stats(student_id=student.id)
        assert stats_response.status_code == requests.codes.ok, (
            f"Expected 200, got {stats_response.status_code}"
        )

        stats = stats_response.json()
        expected_min = min(grades)
        expected_max = max(grades)
        expected_avg = round(sum(grades) / len(grades), 2)

        assert stats["min"] == expected_min, f"Expected min={expected_min}, got {stats['min']}"
        assert stats["max"] == expected_max, f"Expected max={expected_max}, got {stats['max']}"
        assert abs(stats["avg"] - expected_avg) < 0.01, f"Expected avg≈{expected_avg}, got {stats['avg']}"