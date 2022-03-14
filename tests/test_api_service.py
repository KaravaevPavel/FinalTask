import os

import pytest


data = {
  "id": 15,
  "username": "Morlok",
  "firstName": "Pasha",
  "lastName": "Karavaev",
  "email": f"{os.getenv('email')}",
  "password": f"{os.getenv('pass_for_api')}",
  "phone": "+3752598765432",
  "userStatus": 13
}

new_username = "FPWLove"
initial_username = data["username"]


@pytest.fixture(scope="session")
def delete_user_after_test(api_service):
    yield api_service.delete_user(new_username)


@pytest.mark.usefixtures("delete_user_after_test")
class TestAPIService:
    def test_create_user(self, api_service):
        response = api_service.create_user(data)
        assert response.status_code == 200, "User not be created"

    def test_get_userinfo(self, api_service):
        response = api_service.get_user_info_by_user_name(initial_username)
        assert response[0].status_code == 200, response[1]["message"]

    def test_change_username(self, api_service):
        response = api_service.change_username(data, new_username)
        assert response[0].status_code == 200, response[1]["message"]

    def test_check_changed_username(self, api_service):
        response = api_service.get_user_info_by_user_name(new_username)
        assert response[0].status_code == 200, response[1]["message"]
        old_userinfo = data
        new_userinfo = response[1]
        old_userinfo.pop("username")
        new_userinfo.pop("username")
        assert old_userinfo == new_userinfo, "User name not changed"
