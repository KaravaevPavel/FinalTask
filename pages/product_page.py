from finaltask.pages.base_page import BasePage


class ProductPage(BasePage):
    SIZE_WINDOW_LOCATOR = "//select[contains(@name,'Size')]"
    SIZE_DUCK_BY_NAME_LOCATOR = "//option[@value='{}']"
    QUANTITY_INPUT_LOCATOR = "//input[@type='number']"
    ADD_TO_CART_BUTTON_LOCATOR = "//button[@name='add_cart_product']"
    BASKET_BUTTON_LOCATOR = "//a[@class='content']"
    QUANTITY_IN_BASKET_LOCATOR = "//span[@class='quantity' and text()='{}']"

    def add_to_basket(self, *, value, size_duck=None):
        quantity_in_basket_locator = self.QUANTITY_IN_BASKET_LOCATOR.format(value)
        self.set_duck_size(size_duck)
        self.set_value(self.QUANTITY_INPUT_LOCATOR, value)
        self.click(self.ADD_TO_CART_BUTTON_LOCATOR)
        self.is_element_present(quantity_in_basket_locator)

    def set_duck_size(self, size_duck):
        if self.is_element_present(self.SIZE_WINDOW_LOCATOR):
            size_locator = self.SIZE_DUCK_BY_NAME_LOCATOR.format(size_duck)
            self.click(self.SIZE_WINDOW_LOCATOR)
            self.click(size_locator)

    def click_basket(self):
        self.click(self.BASKET_BUTTON_LOCATOR)
