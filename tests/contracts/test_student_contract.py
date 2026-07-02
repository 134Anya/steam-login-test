from faker import Faker

from services.university.helpers.student_helper import StudentHelper
from services.university.models.enums import DegreeEnum

faker = Faker()


class TestStudentContract:
    def test_create_student(self, university_api_utils_admin, temp_group):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        payload = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "degree": DegreeEnum.BACHELOR.value,
            "phone": faker.numerify("+7##########"),
            "group_id": temp_group.id,
        }
        response = helper.post_student(json=payload)
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    def test_get_student(self, university_api_utils_admin, temp_student):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        response = helper.get_student(temp_student.id)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_update_student(self, university_api_utils_admin, temp_student):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        payload = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "degree": DegreeEnum.BACHELOR.value,
            "phone": faker.numerify("+7##########"),
            "group_id": temp_student.group_id,
        }
        response = helper.put_student(temp_student.id, json=payload)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_delete_student(self, university_api_utils_admin, temp_student):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        response = helper.delete_student(temp_student.id)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_get_students_list(self, university_api_utils_admin):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        response = helper.get_students()
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_create_student_without_lastname_negative(self, university_api_utils_admin, temp_group):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        payload = {"first_name": "NoLast", "group_id": temp_group.id}
        response = helper.post_student(json=payload)
        assert response.status_code == 422, f"Expected 422, got {response.status_code}"

    def test_get_non_existent_student_negative(self, university_api_utils_admin):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        all_students = helper.get_students().json()
        non_existent_id = max([s["id"] for s in all_students], default=0) + 1
        response = helper.get_student(non_existent_id)
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
