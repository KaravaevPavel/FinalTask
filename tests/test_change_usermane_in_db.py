import os

user_email = f"{os.getenv('email')}"
expected_user_name = "Pablo"


class TestChangeUsername:
    def test_change_username(self, open_site, login, main_page, user_setting_page, sql_service):
        main_page.click_edit_account_button()
        user_setting_page.change_first_name(expected_user_name)
        user_setting_page.click_save_button()

        username_in_db = sql_service.get_first_name(user_email)

        assert expected_user_name == username_in_db, \
            f"current name in db: {username_in_db}, expected name:{expected_user_name}"
