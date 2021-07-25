from src.pages.base import BasePage
from src.locators.locators import Locators
from test_.TestData.test_data import TestData
import time 
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def SearchForProduct(self, search_key):
        #search for product
        BasePage.fillTextfield(self, Locators.SEARCH_FIELD_ID, search_key)
        BasePage.pressEnter(self, Locators.SEARCH_FIELD_ID)
        return self.driver.current_url, self.driver.page_source

    def SignIn(self, useremail, password):
        BasePage.click(self, Locators.SIGNIN_BTN)
        BasePage.fillTextfield(self, Locators.USER_EMAIL, useremail)
        BasePage.click(self, Locators.CONTINUE_LOGIN_BTN)
        BasePage.fillTextfield(self, Locators.USER_PASSWORD, password)
        BasePage.click(self, Locators.CONTINUE_LOGIN_BTN)
        try:
            error_msg = BasePage.getElementText(self, Locators.PWD_ERROR_MSG)
            if error_msg == TestData.FAIL_TO_LOGIN_TEXT:
                return False
        except:
            time.sleep(3)
            page_source = self.driver.page_source
            if (f"{TestData.LOGIN_WELCOME}" in page_source) and ((f"{TestData.USERNAME}" in page_source)):
                return True
            else:
               return False

