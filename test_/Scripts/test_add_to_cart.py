import sys
import os

sys.path.append(os.getcwd())
import unittest
from src.pages.home_page import HomePage
from src.pages.product_detail_page import ProductDetailPage
from src.pages.search_result_page import SearchResultPage
from src.pages.cart_page import CartPage
from test_.TestData.test_data import TestData
from src.setup.webdriver_setup import WebDriverSetup


class AddToCartCase(WebDriverSetup):

    def test_add_to_cart(self):
        #find product
        product = HomePage(self.driver)
        (url, source) = product.SearchForProduct(TestData.SEARCH_KEYWORD)

        assert f"{TestData.BASE_URL}/search?q={TestData.SEARCH_KEYWORD}" in url
        assert TestData.RESULTS in source

        #get first result
        product = SearchResultPage(self.driver, url)
        (product_title, target_id, pdp_url) = product.GetFirstResult()
        assert (TestData.SEARCH_KEYWORD in product_title) or (TestData.SEARCH_KEYWORD.capitalize() in product_title)

        #is product in stock
        product_pdp = ProductDetailPage(self.driver, pdp_url)
        assert target_id in self.driver.current_url
        assert TestData.PROD_IN_STOCK in self.driver.page_source

        # add product to cart
        cart_url = product_pdp.AddToCart()
        product = CartPage(self.driver, cart_url)
        assert product.isInCart(target_id) == True


if __name__ == "__main__":
    unittest.main()