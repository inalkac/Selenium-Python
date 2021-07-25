from selenium.webdriver.common.by import By

class Locators():
    # Home Page Locators
    SEARCH_FIELD_ID = (By.ID, "global-enhancements-search-query")
    SIGNIN_BTN = (By.XPATH, "//button[contains(@class, 'signin')]")
    USER_EMAIL = (By.ID, "join_neu_email_field")
    USER_PASSWORD = (By.ID, "join_neu_password_field")
    CONTINUE_LOGIN_BTN = (By.NAME, "submit_attempt")
    PROFILE_MENU = (By.XPATH, "//*[@role='menu']")
    PWD_ERROR_MSG = (By.ID, "aria-join_neu_password_field-error")
    #Search Page Locators
    FIRST_PRODUCT_LINK = (By.XPATH, '//a[@data-page-num = "1" and @data-position-num = "1"]')

    #PDP Locators
    VARIATIONS_ID = (By.ID, "variations")
    SUBMIT_BTN_XPATH = (By.XPATH, "//button[@type='submit']")
    VARIATION_SELECTOR_XPATH = (By.XPATH, "//*[contains(@id,'inventory-variation-select')]")
    ADD_TO_CART_BTN = (By.XPATH, "//form[@class='add-to-cart-form']/button")
    VARIATION_OPTION = "option"

    #Cart locators
    ITEM_IN_CART = (By.CSS_SELECTOR, "li[data-cart-listing]")
    ITEM_IN_CART_ID_ATTR = "data-listing-id"
   

