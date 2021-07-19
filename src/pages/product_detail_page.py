from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from src.pages.base import BasePage
from src.locators.locators import Locators


class ProductDetailPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def AddToCart(self):
        if "no-variations" in BasePage.getCssSelectorAttribute(self, Locators.VARIATIONS_ID, "class"):
            BasePage.click(self, Locators.ADD_TO_CART_BTN)
        else: 
            while True:
                i = 0
                variation_selector = self.driver.find_element_by_xpath(f'{Locators.SELECTOR_ATTR}"{i}"]')
                if variation_selector:
                    options = variation_selector.find_element_by_css_selector(Locators.VARIATION_OPTION)
                    options[1].set_attribute("selected")
                else:
                    break
