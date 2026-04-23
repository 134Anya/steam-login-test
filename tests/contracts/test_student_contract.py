import random
import pytest
from faker import Faker

from services.university.helpers.student_helper import StudentHelper
from services.university.models.enums import DegreeEnum
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse

faker = Faker()


class TestStudentContract:
    def test_student_contract_positive(self, university_api_utils_admin, temp_group):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        payload = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice([d.value for d in DegreeEnum]),
            phone=faker.numerify("+7##########"),
            group_id=temp_group.id,
        )

        response = helper.post_student(json=payload.model_dump())

        assert response.status_code == 201, (
            f"Expected 201, got {response.status_code}. Response: {response.text}"
        )

        student = StudentResponse(**response.json())
        assert student.first_name == payload.first_name, (
            f"Name mismatch. Expected {payload.first_name}, got {student.first_name}"
        )
        assert student.group_id == temp_group.id, (
            f"Group ID mismatch. Expected {temp_group.id}, got {student.group_id}"
        )

    def test_update_student_contract_positive(
        self, university_api_utils_admin, temp_student, temp_group
    ):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        payload = StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice([d.value for d in DegreeEnum]),
            phone=faker.numerify("+7##########"),
            group_id=temp_group.id,
        )

        response = helper.put_student(temp_student.id, json=payload.model_dump())

        assert response.status_code == 200, (
            f"Update failed. Expected 200, got {response.status_code}"
        )

        updated_student = StudentResponse(**response.json())
        actual_data = updated_student.model_dump(exclude={"id"})
        expected_data = payload.model_dump()

        assert actual_data == expected_data, (
            f"Data mismatch after update. Expected: {expected_data}, Actual: {actual_data}"
        )

    def test_get_student_by_id(self, university_api_utils_admin, temp_student):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        response = helper.get_student(temp_student.id)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        student = StudentResponse(**response.json())
        assert student.id == temp_student.id, (
            f"ID mismatch. Expected {temp_student.id}, got {student.id}"
        )
        assert student.first_name == temp_student.first_name, (
            f"Name mismatch. Expected {temp_student.first_name}, got {student.first_name}"
        )

    def test_delete_student_contract_positive(
        self, university_api_utils_admin, temp_student
    ):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        response = helper.delete_student(temp_student.id)

        assert response.status_code == 200, (
            f"Delete failed. Expected 200, got {response.status_code}"
        )
        expected_msg = {"detail": "Student deleted"}
        assert response.json() == expected_msg, (
            f"Unexpected message. Expected: {expected_msg}, Actual: {response.json()}"
        )

    def test_get_students_list_contract(self, university_api_utils_admin, temp_student):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        response = helper.get_students()

        assert response.status_code == 200, (
            f"List request failed. Status: {response.status_code}"
        )
        students_raw = response.json()

        assert isinstance(students_raw, list), (
            f"Expected list, got {type(students_raw).__name__}"
        )
        assert len(students_raw) > 0, "Students list is empty"

        student_ids = [s["id"] for s in students_raw]
        assert temp_student.id in student_ids, (
            f"Student ID {temp_student.id} not found in the list"
        )

    def test_create_student_without_lastname_negative(
        self, university_api_utils_admin, temp_group
    ):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        payload = {
            "first_name": faker.first_name(),
            "email": faker.email(),
            "group_id": temp_group.id,
        }

        response = helper.post_student(json=payload)

        assert response.status_code == 422, f"Expected 422, got {response.status_code}"
        assert "last_name" in response.text, (
            f"Error message should mention 'last_name'. Response: {response.text}"
        )

    def test_get_non_existent_student_negative(self, university_api_utils_admin):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        target_id = 999999
        response = helper.get_student(target_id)

        assert response.status_code == 404, (
            f"Expected 404 for ID {target_id}, got {response.status_code}"
        )
        assert response.json() == {"detail": "Student not found"}, (
            f"Wrong error message: {response.json()}"
        )

    def test_create_student_with_non_existent_group_negative(
        self, university_api_utils_admin
    ):
        helper = StudentHelper(api_utils=university_api_utils_admin)
        payload = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email(),
            "degree": random.choice([d.value for d in DegreeEnum]),
            "phone": faker.numerify("+7##########"),
            "group_id": 0,
        }

        response = helper.post_student(json=payload)

        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        assert "group" in response.text.lower(), (
            f"Error message should mention 'group'. Response: {response.text}"
        )
