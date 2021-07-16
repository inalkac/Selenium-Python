from selenium.webdriver.common.by import By

class HomeLocators():
    search_field_id = (By.ID, "global-enhancements-search-query")
    product_link = (By.XPATH, '//a[@data-page-num = "1" and @data-position-num = "1"]')