import pytest
from faker import Faker

from services.university.helpers.group_helper import GroupHelper
from services.university.models.group_request import GroupRequest

faker = Faker()


class TestGroupContract:
    def test_create_group_status(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        payload = GroupRequest(name=faker.word())
        response = group_helper.post_group(json=payload.model_dump())
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    def test_update_group_status(self, university_api_utils_admin, temp_group):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        payload = GroupRequest(name=faker.word())
        response = group_helper.put_group(temp_group.id, json=payload.model_dump())
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_get_group_status(self, university_api_utils_admin, temp_group):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.get_group(temp_group.id)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_delete_group_status(self, university_api_utils_admin, temp_group):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.delete_group(temp_group.id)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_get_groups_list_status(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.get_groups()
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    def test_group_not_found_negative(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        groups_raw = group_helper.get_groups().json()
        non_existent_id = max([g["id"] for g in groups_raw], default=0) + 1
        response = group_helper.get_group(non_existent_id)
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.xfail(reason="Should be 409.")
    def test_delete_group_with_active_student_contract(self, university_api_utils_admin, temp_group, temp_student):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.delete_group(temp_group.id)
        assert response.status_code == 409, f"Expected 409 Conflict, but got {response.status_code}. "
