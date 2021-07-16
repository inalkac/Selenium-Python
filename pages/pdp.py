from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base import BasePage
from locators.pdp_locators import PDPLocators as PDPL


class ProductDetailPage(BasePage):
    def OpenPDP(self, url):
        self.driver.get(url)
    def AddToCart(self):
        if self.driver.find_element_by_id(PDPL.variations):
            print("variations")
        else:
            self.driver.find_element_by_xpath(*PDPL.submit_btn).click()
