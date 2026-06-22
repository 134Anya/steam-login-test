import pytest
from faker import Faker

from services.university.models.enums import DegreeEnum
from services.university.models.grade_request import GradeRequest
from services.university.models.student_request import StudentRequest
from services.university.university_service import UniversityService

faker = Faker()


class TestGradeStats:
    @pytest.fixture
    def stats_setup(self, university_api_utils_admin, temp_student, temp_teacher):
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
            service.create_grade(GradeRequest(student_id=target_student.id, teacher_id=temp_teacher.id, grade=val))

        service.create_grade(GradeRequest(student_id=temp_student.id, teacher_id=temp_teacher.id, grade=2))

        yield service, target_student.id
        service.delete_student(target_student.id)

    def test_student_stats_count(self, stats_setup):
        service, student_id = stats_setup
        stats = service.get_grade_stats(student_id=student_id)
        assert stats.count == 3, f"Wrong grades number. Expected 3, but got {stats.count}"

    def test_student_stats_avg(self, stats_setup):
        service, student_id = stats_setup
        stats = service.get_grade_stats(student_id=student_id)
        assert stats.avg == pytest.approx(4.67, abs=0.01), f"Average score mismatch! Expected 4.67, got {stats.avg}"

    def test_student_stats_min(self, stats_setup):
        service, student_id = stats_setup
        stats = service.get_grade_stats(student_id=student_id)
        assert stats.min == 4, f"Wrong min grade. Expected 4, got {stats.min}"

    def test_student_stats_max(self, stats_setup):
        service, student_id = stats_setup
        stats = service.get_grade_stats(student_id=student_id)
        assert stats.max == 5, f"Wrong max grade. Expected 5, got {stats.max}"
