import pytest
import requests
from faker import Faker

from services.university.helpers.group_helper import GroupHelper
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse

faker = Faker()


class TestGroupContract:
    def test_create_group_positive_contract(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        payload = GroupRequest(name=faker.word())

        response = group_helper.post_group(json=payload.model_dump())

        assert response.status_code == 201, f"Expected 201, got {response.status_code}"

        group = GroupResponse(**response.json())
        assert group.name == payload.name, f"Expected {payload.name}, got {group.name}"
        assert group.id, "Group ID is missing"

    def test_update_group_positive_contract(
        self, university_api_utils_admin, temp_group
    ):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        payload = GroupRequest(name=faker.word())

        response = group_helper.put_group(temp_group.id, json=payload.model_dump())

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        group = GroupResponse(**response.json())

        assert group.model_dump(exclude={"id"}) == payload.model_dump(), (
            f"Data mismatch. Expected: {payload.model_dump()}, Actual: {group.model_dump(exclude={'id'})}"
        )

    def test_delete_group_contract(self, university_api_utils_admin, temp_group):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.delete_group(temp_group.id)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        assert response.json() == {"detail": "Group deleted"}, (
            f"Unexpected message: {response.json()}"
        )

    def test_get_group_contract(self, university_api_utils_admin, temp_group):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.get_group(temp_group.id)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        group = GroupResponse(**response.json())
        assert group.id == temp_group.id, (
            f"ID mismatch. Expected {temp_group.id}, got {group.id}"
        )
        assert group.name == temp_group.name, (
            f"Name mismatch. Expected {temp_group.name}, got {group.name}"
        )

    def test_get_groups_list_contract(self, university_api_utils_admin, temp_group):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.get_groups()

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        groups_raw = response.json()

        group_ids = [g["id"] for g in groups_raw]
        assert temp_group.id in group_ids, (
            f"ID {temp_group.id} not found in {group_ids}"
        )

    def test_group_not_found_negative(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        target_id = 999999
        response = group_helper.get_group(target_id)

        assert response.status_code == 404, (
            f"Expected 404 for ID {target_id}, got {response.status_code}"
        )
        assert response.json()["detail"] == "Group not found", (
            f"Unexpected error msg: {response.json()}"
        )
