import re
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _get_locator_by_type(self, locator):
        string = locator
        prefixes = ["//", ".", "("]
        result = string.startswith(tuple(prefixes))
        if result:
            return By.XPATH
        return By.CSS_SELECTOR

    def open_url(self, url):
        self.driver.get(url)

    def _element(self, locator, timeout_sec=2):
        locator_by_type = self._get_locator_by_type(locator)

        element = WebDriverWait(self.driver, timeout_sec)\
            .until(expected_conditions.presence_of_element_located((locator_by_type, locator)))
        return element

    def click(self, locator):
        element = self._element(locator)
        element.click()

    def find_elements(self, locator, timeout=2):
        by_type = self._get_locator_by_type(locator)
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located((by_type, locator))
        )
        return element

    def get_text(self, locator):
        element = self._element(locator)
        return element.text

    def enter_text(self, locator, text):
        element = self._element(locator)
        element.send_keys(text)

    def get_price(self, locator):
        price = self.get_text(locator)
        price = re.findall("[0-9.]+", price)
        return float(price[0])

    def is_element_present(self, locator):
        try:
            self._element(locator)
            return True
        except TimeoutException:
            return False

    def clear_input_window(self, locator):
        element = self._element(locator)
        element.clear()

    def set_value(self, input_locator, value):
        self.clear_input_window(input_locator)
        self.enter_text(input_locator, value)

    def get_elements_count(self, locator):
        return len(self.find_elements(locator))

    def get_attribute(self, locator, attribute):
        element = self._element(locator)
        return element.get_attribute(attribute)

    def go_to_main_page(self):
        self.open_url("//img[@alt='My Store']")
