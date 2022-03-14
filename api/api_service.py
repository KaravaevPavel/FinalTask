import json
import requests


class APIService:
    BASE_URL = "https://petstore.swagger.io/v2/user/"

    def _get(self, end_point, expected_status_code=200):
        url = self.BASE_URL + end_point
        response = requests.get(url)

        assert response == expected_status_code, "Status code is not correct"
        return json.loads(response.text)

    def create_user(self, data):
        json_data = json.dumps(data)
        header = {'Content-Type': 'application/json'}
        response = requests.request("POST", self.BASE_URL, headers=header, data=json_data)
        return response

    def get_user_info_by_user_name(self, username):
        user_url = self.BASE_URL + username
        response = requests.request("GET", user_url)
        info = json.loads(response.text)
        return [response, info]

    def change_username(self, old_data, new_username):
        user_url = self.BASE_URL + old_data["username"]
        new_data = old_data.copy()
        new_data["username"] = new_username
        json_data = json.dumps(new_data)
        header = {'Content-Type': 'application/json'}
        response = requests.request("PUT", user_url, data=json_data, headers=header)
        info = json.loads(response.text)

        return [response, info]

    def delete_user(self, username):
        user_url = self.BASE_URL + username
        requests.request("DELETE", user_url)
