from src.pages.base import BasePage
from src.locators.locators import Locators
import time


class ProductDetailPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def AddToCart(self):
        if "no-variations" not in BasePage.getCssSelectorAttribute(self, Locators.VARIATIONS_ID, "class"):
            try:
                variations = BasePage.getDropDownElements(self, Locators.VARIATION_SELECTOR_XPATH)
                for i in range(0, len(variations)):
                    items = BasePage.getDropDownElements(self, Locators.VARIATION_SELECTOR_XPATH)
                    BasePage.selectDropdownOption(self, items[i], 1)
                    time.sleep(3)
            except:
                pass 
        BasePage.click(self, Locators.ADD_TO_CART_BTN)
        return self.driver.current_url
