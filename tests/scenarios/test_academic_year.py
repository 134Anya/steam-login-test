import random

import pytest
from faker import Faker

from services.university.models.enums import DegreeEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.student_request import StudentRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestAcademicYear:
    def test_academic_year(
        self,
        university_api_utils_admin,
        temp_group,
        temp_student,
        temp_teacher,
        request,
    ):

        service = UniversityService(api_utils=university_api_utils_admin)

        target_payload = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice([d.value for d in DegreeEnum]),
            phone=faker.numerify("+7##########"),
            group_id=temp_group.id,
        )
        target_student = service.create_student(target_payload)

        target_grades = [5, 4, 5]
        for val in target_grades:
            service.create_grade(
                GradeRequest(
                    student_id=target_student.id, teacher_id=temp_teacher.id, grade=val
                )
            )

        for val in [2, 2]:
            service.create_grade(
                GradeRequest(
                    student_id=temp_student.id, teacher_id=temp_teacher.id, grade=val
                )
            )

        stats = service.get_grade_stats(student_id=target_student.id)
        assert stats.count == 3, f"Expected 3 grades, but found {stats.count}"

        assert stats.avg == pytest.approx(4.67, abs=0.01), (
            f"Average score mismatch! Expected 4.67, got {stats.avg}"
        )
        assert stats.min == 4, f"Wrong min grade. Expected 4, got {stats.min}"
        assert stats.max == 5, f"Wrong max grade. Expected 5, got {stats.max}"
