from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(by_locator)).click()

    def fillTextfield(self, by_locator, text):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def pressEnter(self, by_locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def getLink (self, by_locator):
        wait = WebDriverWait(self.driver, 5)
        link = wait.until(EC.presence_of_element_located(by_locator))
        return link

    def getElements(self, by_locator):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_all_elements_located(by_locator))

    def getCssSelectorAttribute(self, by_locator, attr_name):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_element_located(by_locator)).get_attribute(attr_name)
    def getElementText(self, by_locator):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_element_located(by_locator)).text

    def getDropDownElements(self, by_locator):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(EC.visibility_of_all_elements_located(by_locator))

    def selectDropdownOption(self, webelement, option_no):
        selector = Select(webelement)
        selector.select_by_index(option_no)

    