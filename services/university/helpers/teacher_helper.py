import requests

from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    ENDPOINT_PREFIX = "/teachers/"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}"

    def get_teachers(self, params: dict = None) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, params=params)
        return response

    def post_teachers(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_teacher_by_id(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.get(f"{self.ROOT_ENDPOINT}{teacher_id}/")
        return response

    def put_teachers(self, teacher_id: int, json: dict) -> requests.Response:
        response = self.api_utils.put(f"{self.ROOT_ENDPOINT}{teacher_id}/", json=json)
        return response

    def delete_teachers(self, teacher_id: int) -> requests.Response:
        response = self.api_utils.delete(f"{self.ROOT_ENDPOINT}{teacher_id}/")
        return response
