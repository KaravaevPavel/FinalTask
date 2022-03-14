from finaltask.pages.base_page import BasePage


class MainPage(BasePage):
    USER_NAME_LOCATOR = "//input[@name='email']"
    USER_PASSWORD_LOCATOR = "//input[@name='password']"
    LOGIN_BUTTON_LOCATOR = "//button[@name='login']"
    EDIT_ACCOUNT_BUTTON = "//aside//li[3]/a[@href]"
    PRODUCT_BY_NAME_LOCATOR = "//div[@id='box-most-popular']//div[text()='{}']"

    def enter_user_name(self, user_name):
        self.enter_text(self.USER_NAME_LOCATOR, user_name)

    def enter_user_password(self, password):
        self.enter_text(self.USER_PASSWORD_LOCATOR, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON_LOCATOR)

    def login(self, user_name, password):
        self.enter_user_name(user_name)
        self.enter_user_password(password)
        self.click_login_button()

    def click_edit_account_button(self):
        self.click(self.EDIT_ACCOUNT_BUTTON)

    def select_product_by_name(self, name):
        selected_product = self.PRODUCT_BY_NAME_LOCATOR.format(name)
        self.click(selected_product)
