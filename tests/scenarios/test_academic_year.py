import pytest
from faker import Faker

from services.university.models.enums import DegreeEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.student_request import StudentRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestGradeStats:
    def test_student_stats_count(
        self, university_api_utils_admin, temp_student, temp_teacher
    ):
        service = UniversityService(api_utils=university_api_utils_admin)

        payload = StudentRequest(
            first_name="Target",
            last_name="Student",
            email=faker.email(),
            degree=DegreeEnum.BACHELOR.value,
            phone=faker.numerify("+7##########"),
            group_id=temp_student.group_id,
        )
        target_student = service.create_student(payload)
        for val in [5, 4, 5]:
            service.create_grade(
                GradeRequest(
                    student_id=target_student.id, teacher_id=temp_teacher.id, grade=val
                )
            )

        service.create_grade(
            GradeRequest(
                student_id=temp_student.id, teacher_id=temp_teacher.id, grade=2
            )
        )
        stats = service.get_grade_stats(student_id=target_student.id)
        assert stats.count == 3, f"Expected 3 grades, but found {stats.count}"

    def test_student_stats_avg(
        self, university_api_utils_admin, temp_student, temp_teacher
    ):
        service = UniversityService(api_utils=university_api_utils_admin)
        payload = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=DegreeEnum.BACHELOR.value,
            phone=faker.numerify("+7##########"),
            group_id=temp_student.group_id,
        )
        target_student = service.create_student(payload)

        for val in [5, 4, 5]:
            service.create_grade(
                GradeRequest(
                    student_id=target_student.id, teacher_id=temp_teacher.id, grade=val
                )
            )
        stats = service.get_grade_stats(student_id=target_student.id)
        assert stats.avg == pytest.approx(4.67, abs=0.01), (
            f"Wrong average. Got {stats.avg}"
        )

    def test_student_stats_min(
        self, university_api_utils_admin, temp_student, temp_teacher
    ):
        service = UniversityService(api_utils=university_api_utils_admin)

        payload = StudentRequest(
            first_name="Target",
            last_name="Student",
            email=faker.email(),
            degree=DegreeEnum.BACHELOR.value,
            phone=faker.numerify("+7##########"),
            group_id=temp_student.group_id,
        )
        target_student = service.create_student(payload)

        for val in [5, 4, 5]:
            service.create_grade(
                GradeRequest(
                    student_id=target_student.id, teacher_id=temp_teacher.id, grade=val
                )
            )

        stats = service.get_grade_stats(student_id=target_student.id)
        assert stats.min == 4, f"Expected min grade 4, but got {stats.min}"

    def test_student_stats_max(
        self, university_api_utils_admin, temp_student, temp_teacher
    ):
        service = UniversityService(api_utils=university_api_utils_admin)

        payload = StudentRequest(
            first_name="Target",
            last_name="Student",
            email=faker.email(),
            degree=DegreeEnum.BACHELOR.value,
            phone=faker.numerify("+7##########"),
            group_id=temp_student.group_id,
        )
        target_student = service.create_student(payload)

        for val in [5, 4, 5]:
            service.create_grade(
                GradeRequest(
                    student_id=target_student.id, teacher_id=temp_teacher.id, grade=val
                )
            )
        stats = service.get_grade_stats(student_id=target_student.id)

        assert stats.max == 5, f"Expected max grade 5, but got {stats.max}"
