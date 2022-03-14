import os

import pytest

email = f"{os.getenv('email')}"
password = f"{os.getenv('pass_for_litecart')}"
name_product = "Blue Duck"
initial_quantity = 1
set_quantity = 3


@pytest.fixture(scope="session")
def setup_for_basket(open_site, main_page, product_page, basket_page):
    main_page.login(email, password)
    main_page.select_product_by_name(name_product)
    product_page.add_to_basket(value=initial_quantity)
    product_page.click_basket()
    basket_page.choose_count_ducks(set_quantity)


@pytest.mark.usefixtures("setup_for_basket")
class TestBasket:
    def test_add_product(self, basket_page):
        current_quantity = basket_page.get_quantity_product()

        assert current_quantity == set_quantity, \
            f"Current quantity: {current_quantity}. Expected: {set_quantity}"

    def test_correctness_price(self, basket_page):
        unit_cost = basket_page.get_unit_cost()
        expected_cost = basket_page.get_total_price()
        correctness_price = unit_cost * basket_page.get_quantity_product()

        assert expected_cost == correctness_price, \
            f"Correctness_price = {correctness_price}. But on site we see price{expected_cost}"

    def test_clear_basket(self, basket_page):
        basket_page.remove_product_from_basket()
        assert basket_page.check_the_basket_is_empty(), \
            "Basket not empty"
