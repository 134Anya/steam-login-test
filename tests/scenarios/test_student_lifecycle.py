import pytest
from faker import Faker

from services.university.models.grade_request import GradeRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestStudentLifecycle:
    def test_student_grade_avg(
        self, university_api_utils_admin, temp_teacher, temp_student
    ):
        service = UniversityService(api_utils=university_api_utils_admin)
        student_id = temp_student.id
        for val in [5, 4, 3]:
            service.create_grade(
                GradeRequest(
                    student_id=student_id, teacher_id=temp_teacher.id, grade=val
                )
            )

        stats = service.get_grade_stats(student_id=student_id)
        assert stats.avg == pytest.approx(4.0), (
            f"Wrong average calculation. Expected 4.0, but got {stats.avg}"
        )

    def test_student_grade_count(
        self, university_api_utils_admin, temp_teacher, temp_student
    ):
        service = UniversityService(api_utils=university_api_utils_admin)
        student_id = temp_student.id

        for val in [5, 4, 3]:
            service.create_grade(
                GradeRequest(
                    student_id=student_id, teacher_id=temp_teacher.id, grade=val
                )
            )
        stats = service.get_grade_stats(student_id=student_id)
        assert stats.count == 3, (
            f"Wrong grades number. Expected 3, but got {stats.count}"
        )
