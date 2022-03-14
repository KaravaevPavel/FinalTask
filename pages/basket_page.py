from finaltask.pages.base_page import BasePage


class BasketPage(BasePage):
    COUNT_OF_DUCKS_LOCATOR = "//td[.='3']"
    UNIT_COST_LOCATOR = "//td[@class='unit-cost']"
    TOTAL_COST_LOCATOR = "//strong[contains(.,'$') or contains(.,'€')]"
    REMOVE_BUTTON_LOCATOR = "//button[@name='remove_cart_item']"
    INSCRIPTION_WHEN_BASKET_IS_EMPTY_LOCATOR = "//em[.='There are no items in your cart.']"
    QUANTITY_INPUT_LOCATOR = "//input[@name='quantity']"
    UPDATE_BUTTON_LOCATOR = "//button[@value='Update']"
    WAITING_QUANTITY_LOCATOR = "//input[@value='{}']"

    def remove_product_from_basket(self):
        count_products = self.get_elements_count(self.REMOVE_BUTTON_LOCATOR)
        for element in range(count_products):
            self.click(self.REMOVE_BUTTON_LOCATOR)

    def check_the_basket_is_empty(self):
        if self.is_element_present(self.INSCRIPTION_WHEN_BASKET_IS_EMPTY_LOCATOR):
            return True
        else:
            return False

    def get_quantity_product(self):
        attribute = self.get_attribute(self.QUANTITY_INPUT_LOCATOR, "value")
        return int(attribute)

    def get_unit_cost(self):
        return self.get_price(self.UNIT_COST_LOCATOR)

    def get_total_price(self):
        return self.get_price(self.TOTAL_COST_LOCATOR)

    def choose_count_ducks(self, count):
        new_count_ducks = self.WAITING_QUANTITY_LOCATOR.format(count)
        self.set_value(self.QUANTITY_INPUT_LOCATOR, count)
        self.click(self.UPDATE_BUTTON_LOCATOR)
        self.is_element_present(new_count_ducks)
        self.is_element_present(new_count_ducks)
