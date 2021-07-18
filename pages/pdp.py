from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base import BasePage
from locators.pdp_locators import PDPLocators as PDPL


class ProductDetailPage(BasePage):
    def OpenPDP(self, url):
        self.driver.get(url)
    def AddToCart(self):
        if "no-variations" in self.driver.find_element_by_id(PDPL.variations_id).get_attribute("class"):
            self.driver.find_element_by_xpath(PDPL.submit_btn).click()
        else: 
            while True:
                i = 0
                variation_selector = self.driver.find_element_by_xpath(f'{PDPL.selector_attr}"{i}"]')
                if variation_selector:
                    options = variation_selector.find_element_by_css_selector('option')
                    options[1].set_attribute("selected")
                else:
                    break
