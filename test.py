import logging
logging.basicConfig(level=logging.INFO)

import unittest
from tests import testPathHandlingFunc



if __name__ == "__main__":
    logging.info(" [Starting Tests]")
    unittest.main(testPathHandlingFunc, verbosity=2)