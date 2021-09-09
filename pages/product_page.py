import time

from ..base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text


    def basket_value(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text


    def book_in_basket(self, book, basket):
        assert book in basket, f'Book is not at the basket that costs {basket}'

    def book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def basket_book(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_BOOK).text

    def basket_has_book(self, book, basket):
        assert book in basket, f"Book's name does not match the name of the book in the basket"

    def add_to_basket(self):
        self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON)
        self.click_button(*ProductPageLocators.ADD_BASKET_BUTTON)
        self.solve_quiz_and_get_code()
        self.book_in_basket(self.book_price(), self.basket_value())
        self.basket_has_book(self.book_name(), self.basket_book())

