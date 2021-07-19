from src.pages.base import BasePage
from src.locators.locators import Locators
from test_.TestData.test_data import TestData
 
class SearchResultPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    def GetFirstResult(self):
        product = BasePage.getLink(self, Locators.FIRST_PRODUCT_LINK)
        product_title = product.get_attribute("title")
        pdp_url = product.get_attribute("href")
        product_id = product.get_attribute("target")
        product_id = product_id.split(".")[1]
        return product_title, product_id, pdp_url