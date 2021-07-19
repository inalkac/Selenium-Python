import sys
import os
sys.path.append(os.getcwd())
import unittest
from src.pages.home_page import HomePage
from src.pages.product_detail_page import ProductDetailPage
from src.pages.search_result_page import SearchResultPage
from test_.TestData.test_data import TestData
from selenium import webdriver
from src.setup.webdriver_setup import WebDriverSetup


class AddToCartCase(WebDriverSetup):

    def test_add_to_cart(self):
        #find product
        product = HomePage(self.driver)
        search_for = "key"
        (url, source) = product.SearchForProduct(search_for)

        assert f"{TestData.BASE_URL}/search?q={search_for}" in url
        assert "results" in source

        #get first result
        product = SearchResultPage(self.driver, url)
        (product_title, target_id, pdp_url) = product.GetFirstResult()
        assert (search_for in product_title) or (search_for.capitalize() in product_title)

        #is product in stock
        product_pdp = ProductDetailPage(self.driver, pdp_url)
        
        assert target_id in self.driver.current_url
        assert 'Add to cart' in self.driver.page_source

        product_pdp.AddToCart()
        

if __name__ == "__main__":
    unittest.main()