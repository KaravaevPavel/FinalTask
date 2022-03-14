from finaltask.pages.base_page import BasePage


class UserSettingPage(BasePage):
    SAVE_BUTTON_LOCATOR = "//button[@name='save']"
    FIRST_NAME_INPUT_LOCATOR = "//input[@name='firstname']"
    def change_first_name(self, new_first_name):
        self.set_value(self.FIRST_NAME_INPUT_LOCATOR, new_first_name)

    def click_save_button(self):
        self.click(self.SAVE_BUTTON_LOCATOR)
