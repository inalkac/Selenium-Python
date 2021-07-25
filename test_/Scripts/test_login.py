import sys
import os

sys.path.append(os.getcwd())
import unittest
from src.pages.home_page import HomePage
from src.setup.webdriver_setup import WebDriverSetup
from test_.TestData.test_data import TestData

class Login(WebDriverSetup):

    def test_login(self):
        page = HomePage(self.driver)
        assert page.SignIn(TestData.USEREMAIL, TestData.PASSWORD) == True
        assert page.SignIn(f"a{TestData.USEREMAIL}", TestData.PASSWORD) == False
        assert page.SignIn({TestData.USEREMAIL}, f"{TestData.PASSWORD}1") == False

if __name__ == "__main__":
    unittest.main()