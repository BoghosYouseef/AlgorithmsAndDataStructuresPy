import logging
logging.basicConfig(level=logging.INFO)
import os
import sys
import unittest
from tests import testDoublyLinkedListClass, testPathHandlingFunc 

# code copied and modified from https://dnmtechs.com/running-unittest-main-for-all-source-files-in-a-subdirectory/

modules = [
    testDoublyLinkedListClass,
    testPathHandlingFunc
]
def run_tests():
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    for module in modules:
        test_suite.addTests(test_loader.loadTestsFromModule(module))
    
    # Run the test suite
    exitCode = unittest.TextTestRunner(verbosity=2).run(test_suite).wasSuccessful()
    return exitCode

if __name__ == '__main__':
    exitCode = run_tests() # returns True or False
    sys.exit(not exitCode)   # should be True