import time

from ..base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def book_price(self):
        value = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        return value

    def basket_value(self):
        value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text.split(' ')[2].split('\n')[0]
        return value

    def book_in_basket(self, book, basket):
        assert book == basket, f'Book is not at the basket that costs {basket}'

    def book_name(self):
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return name

    def basket_book(self):
        basket_books = self.browser.find_element(*ProductPageLocators.BASKET_BOOK).text
        return basket_books

    def basket_has_book(self, book, basket):
        assert book == basket, f"Book's name does not match the name of the book in the basket"

    def success_message_is_presented(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), 'No success message'

    def add_to_basket(self):
        self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON)
        self.click_button(*ProductPageLocators.ADD_BASKET_BUTTON)
        self.success_message_is_presented()
        self.book_in_basket(self.book_price(), self.basket_value())
        self.basket_has_book(self.book_name(), self.basket_book())

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is here!'

    def success_message_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message did not disappear!'