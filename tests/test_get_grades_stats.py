import random
import pytest
from faker import Faker
from services.university.university_service import UniversityService
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.models.grade_request import GradeRequest
from services.university.models.enums import DegreeEnum, SubjectEnum
from services.university.models.grade_constants import MAX_GRADE, MIN_GRADE
from services.university.models.grade_stats_response import GradeStatsResponse

faker = Faker()


@pytest.fixture(scope="module")
def setup_student_grades(university_api_utils_admin):
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

    grades = [random.randint(MIN_GRADE, MAX_GRADE) for _ in range(5)]
    for g in grades:
        university_service.create_grade(
            GradeRequest(
                teacher_id=teacher.id,
                student_id=student.id,
                grade=g,
            )
        )

    stats_response = university_service.grade_helper.get_stats(student_id=student.id)

    return {
        "service": university_service,
        "student": student,
        "grades": grades,
        "stats_response": stats_response,
    }


def test_get_grades_stats_contract(setup_student_grades):
    stats_response = setup_student_grades["stats_response"]
    GradeStatsResponse(**stats_response.json())
    assert stats_response.status_code == 200, f"Expected 200, got {stats_response.status_code}"


def test_min_grade_value(setup_student_grades):
    grades = setup_student_grades["grades"]
    stats = GradeStatsResponse(**setup_student_grades["stats_response"].json())

    expected_min = min(grades)
    assert stats.min == expected_min, f"Expected min={expected_min}, got {stats.min}"


def test_max_grade_value(setup_student_grades):
    grades = setup_student_grades["grades"]
    stats = GradeStatsResponse(**setup_student_grades["stats_response"].json())

    expected_max = max(grades)
    assert stats.max == expected_max, f"Expected max={expected_max}, got {stats.max}"


def test_avg_grade_value(setup_student_grades):
    grades = setup_student_grades["grades"]
    stats = GradeStatsResponse(**setup_student_grades["stats_response"].json())

    expected_avg = round(sum(grades) / len(grades), 2)
    actual_avg = round(stats.avg, 2)
    assert actual_avg == expected_avg, f"Expected avg={expected_avg}, got {actual_avg}"