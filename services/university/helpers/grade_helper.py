import requests
from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ROOT_ENDPOINT = "/grades/"
    STATS_ENDPOINT = f"{ROOT_ENDPOINT}stats/"

    def get_grades(self, params: dict | None = None) -> requests.Response:
        return self.api_utils.get(self.ROOT_ENDPOINT, params=params)

    def post_grade(self, data: dict) -> requests.Response:
        return self.api_utils.post(self.ROOT_ENDPOINT, data=data)

    def get_grade_stats(
        self,
        student_id: int | None = None,
        teacher_id: int | None = None,
        group_id: int | None = None,
    ) -> requests.Response:
        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id

        return self.api_utils.get(self.STATS_ENDPOINT, params=params)

    def put_grade(self, grade_id: int, json: dict) -> requests.Response:
        return self.api_utils.put(f"{self.ROOT_ENDPOINT}{grade_id}/", json=json)

    def delete_grade(self, grade_id: int) -> requests.Response:
        return self.api_utils.delete(f"{self.ROOT_ENDPOINT}{grade_id}/")
