from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base import BasePage
from locators.home_locators import HomeLocators as HL

class HomePage(BasePage):
    def OpenHomePage(self):
        self.driver.get("https://www.etsy.com/")
        self.driver.maximize_window()

    def SearchForProduct(self, search_key):
        #search for product
        self.driver.delete_all_cookies()
        wait = WebDriverWait(self.driver, 5)
        search_field = wait.until(EC.presence_of_element_located(HL.search_field_id))
        search_field.send_keys(search_key)
        search_field.send_keys(Keys.ENTER)
        return self.driver.current_url, self.driver.page_source
 
    def GetFirstResult(self):
        wait = WebDriverWait(self.driver, 5)
        product = wait.until(EC.presence_of_element_located(HL.product_link))
        product_title = product.get_attribute("title")
        pdp_url = product.get_attribute("href")
        product_id = product.get_attribute("target")
        product_id = product_id.split(".")[1]
        return product_title, product_id, pdp_url