from src.pages.base import BasePage
from src.locators.locators import Locators
from test_.TestData.test_data import TestData
 
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def SearchForProduct(self, search_key):
        #search for product
        BasePage.fillTextfield(self, Locators.SEARCH_FIELD_ID, search_key)
        BasePage.pressEnter(self, Locators.SEARCH_FIELD_ID)
        return self.driver.current_url, self.driver.page_source
 