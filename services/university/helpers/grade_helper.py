from typing import Optional

import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades/"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}"

    def get_grades(self, params: dict = None) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, params=params)
        return response

    def post_grade(self, data: dict) -> requests.Response:
        return self.api_utils.post(self.ROOT_ENDPOINT, data=data)

    def get_grade_stats(
        self,
        student_id: Optional[int] = None,
        teacher_id: Optional[int] = None,
        group_id: Optional[int] = None,
    ) -> requests.Response:

        params = {}
        if student_id is not None:
            params["student_id"] = student_id
        if teacher_id is not None:
            params["teacher_id"] = teacher_id
        if group_id is not None:
            params["group_id"] = group_id
        response = self.api_utils.get(f"{self.ROOT_ENDPOINT}stats/", params=params)
        return response

    def put_grade(self, grade_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(f"{self.ROOT_ENDPOINT}{grade_id}/", json=json)
        return response

    def delete_grade(self, grade_id: int) -> requests.Response:
        response = self.api_utils.delete(f"{self.ROOT_ENDPOINT}{grade_id}/")
        return response
