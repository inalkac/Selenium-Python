import sys
import os
sys.path.append(os.getcwd())
 
from unittest import TestLoader, TestSuite, TextTestRunner
from test_.Scripts.test_add_to_cart import AddToCartCase

 
import testtools as testtools
 
if __name__ == "__main__":
 
    test_loader = TestLoader()
    
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(AddToCartCase),
        #more test cases
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
 
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
