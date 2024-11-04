import unittest
import pathlib
from utils.pathHandling import getDataStructuresAbsPath


class TestgetDataStructuresAbsPath(unittest.TestCase):

    def testEqualDataStructuresAbsPath(self):
        self.assertEqual(getDataStructuresAbsPath(), pathlib.Path(str( pathlib.Path(__file__).parent.parent.resolve()) + "/dataStructures"))
    
    def testIsInstanceOfPathLibDir(self):
        self.assertIsInstance(getDataStructuresAbsPath(), pathlib.Path().__class__)
    
    def testExistsDir(self):
        self.assertEqual(pathlib.Path('dataStructures').is_dir(), True)