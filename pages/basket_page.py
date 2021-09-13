from .locators import BasketPageLocators
from ..base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET)

    def empty_basket_has_message_about_emptiness(self):
        assert self.message(*BasketPageLocators.EMPTY_PAGE_MESSAGE).text == 'Your basket is empty. Continue shopping', 'Basket is not empty'

    def total_price_of_basket_is_right(self):
        prices = self.browser.find_elements(*BasketPageLocators.ITEM_IN_BASKET).text
        total = 0
        for book_price in prices:
            total += int(book_price)
        order_total = self.browser.find_element(*BasketPageLocators.ORDER_TOTAL)
        assert total == int(order_total), f'Order total {order_total} is not equal to the sum of the books {total}'
