from selenium.webdriver.common.by import By

class Locators():
    # Home Page Locators
    SEARCH_FIELD_ID = (By.ID, "global-enhancements-search-query")

    #Search Page Locators
    FIRST_PRODUCT_LINK = (By.XPATH, '//a[@data-page-num = "1" and @data-position-num = "1"]')

    #PDP Locators
    VARIATIONS_ID = (By.ID, "variations")
    SUBMIT_BTN_XPATH = (By.XPATH, "//button[@type='submit']")
    SELECTOR_ATTR = '//select[@data-buy-box-select='
    ADD_TO_CART_BTN = (By.XPATH, "//form[@class='add-to-cart-form']/button")
    VARIATION_OPTION = "option"