from .locators import BasketPageLocators
from ..base_page import BasePage


class BasketPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET)

    def empty_basket_has_message_about_emptiness(self):
        assert self.message(*BasketPageLocators.EMPTY_PAGE_MESSAGE).text == 'Your basket is empty. Continue shopping'