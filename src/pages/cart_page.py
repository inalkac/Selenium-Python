from src.pages.base import BasePage
from src.locators.locators import Locators

class CartPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def isInCart(self, product_id):
        try:
            item_list = BasePage.getElements(self, Locators.ITEM_IN_CART)
            for i in item_list:
                if i.get_attribute(Locators.ITEM_IN_CART_ID_ATTR) == product_id:
                    return True
            return False
        except:
            pass
    def isEmpty(self):
        try:
            item_list = BasePage.getElements(self, Locators.ITEM_IN_CART)
            return len(item_list) == 0
        except:
            pass