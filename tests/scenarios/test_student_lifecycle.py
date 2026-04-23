import pytest
from faker import Faker

from logger.logger import Logger
from services.university.models.grade_request import GradeRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestStudentLifecycle:
    def test_student_grade_stats(
        self, university_api_utils_admin, temp_teacher, temp_student
    ):
        service = UniversityService(api_utils=university_api_utils_admin)
        student_id = temp_student.id
        Logger.info(f"### Step 1: Adding grades for student {student_id}")
        grades = [5, 4, 3]
        for val in grades:
            service.create_grade(
                GradeRequest(
                    student_id=student_id, teacher_id=temp_teacher.id, grade=val
                )
            )

        Logger.info("### Step 2: Fetching and checking statistics")

        stats = service.get_grade_stats(student_id=student_id)

        assert stats.avg == pytest.approx(4.0), (
            f"Wrong calculation. Expected 4.0, but got {stats.avg}"
        )
        assert stats.count == 3, (
            f"Wrong grades number. Expected 3, but got {stats.count}"
        )
