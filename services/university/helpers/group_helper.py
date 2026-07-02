import requests

from services.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups/"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}"

    def post_group(self, json: dict) -> requests.Response:
        return self.api_utils.post(self.ROOT_ENDPOINT, json=json)

    def get_group(self, group_id: int) -> requests.Response:
        return self.api_utils.get(f"{self.ROOT_ENDPOINT}{group_id}/")

    def get_groups(self) -> requests.Response:
        return self.api_utils.get(self.ROOT_ENDPOINT)

    def delete_group(self, group_id) -> requests.Response:
        return self.api_utils.delete(f"{self.ROOT_ENDPOINT}{group_id}/")

    def put_group(self, group_id: int, json: dict) -> requests.Response:
        return self.api_utils.put(f"{self.ROOT_ENDPOINT}{group_id}/", json=json)
