import pytest
import requests

from services.university.university_service import UniversityService


class TestGroupNegative:
    @pytest.mark.xfail
    def test_delete_group_with_active_student(
        self, university_api_utils_admin, temp_group, temp_student
    ):
        service = UniversityService(api_utils=university_api_utils_admin)

        with pytest.raises(requests.exceptions.HTTPError) as err:
            service.delete_group(temp_group.id)

        response = err.value.response
        assert response.status_code == 409, (
            f"Expected to get (400/409), but got {response.status_code}. "
            f"The group is deleted with active students"
        )
