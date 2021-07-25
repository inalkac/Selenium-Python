import os

class TestData():
    CHROME_EXECUTABLE_PATH=f"{os.curdir}/drivers/chromedriver.exe"
    BASE_URL = "https://www.etsy.com"
    HOME_PAGE_TITLE = "Etsy - Shop for handmade, vintage, custom, and unique gifts for everyone"
    NO_RESULTS_TEXT = "No results found."
    CART_EMPTY = "Your cart is empty"
    SEARCH_KEYWORD = "key"
    RESULTS = "results"
    PROD_IN_STOCK = 'In stock' 
    USEREMAIL = "for.testing.cla@gmail.com"
    PASSWORD = "password"
    USERNAME = "user"
    FAIL_TO_LOGIN_TEXT = "Password was incorrect"
    LOGIN_WELCOME = "Welcome"
