import unittest
import random
from parameterized import parameterized
from dataStructures.nodes import Node, BinaryNode
from algorithms.BFS import BFS



class TestBFS(unittest.TestCase):

    def testIntInput(self):
        root = BinaryNode(value=10)
        for i in range(0,20):
            root.insert(i)

        
        element5 = BFS.find(rootNode=root,element=5)
        self.assertEqual(element5.value, 5)