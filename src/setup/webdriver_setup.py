import unittest
from selenium import webdriver 
from test_.TestData.test_data import TestData

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
 
    def tearDown(self):
        if (self.driver != None):
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()