import unittest
import os
from pages.home import HomePage
from pages.pdp import ProductDetailPage
from selenium import webdriver


class AddToCartCase(unittest.TestCase):
    def setUp(self):
        path = f"{os.curdir}/drivers/chromedriver.exe"
        self.driver = webdriver.Chrome(path)
        

    def test_add_to_cart(self):
        #find product
        product = HomePage(self.driver)
        product.OpenHomePage()
        search_for = "key"
        (url, source) = product.SearchForProduct(search_for)

        assert f"https://www.etsy.com/search?q={search_for}" in url
        assert "results" in source

        (product_title, target_id, pdp_url) = product.GetFirstResult()
        assert (search_for in product_title) or (search_for.capitalize() in product_title)

        #is product in stock
        product_pdp = ProductDetailPage(self.driver)
        product_pdp.OpenPDP(pdp_url)

        assert target_id in self.driver.current_url
        assert 'Add to cart' in self.driver.page_source

        product_pdp.AddToCart()
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()