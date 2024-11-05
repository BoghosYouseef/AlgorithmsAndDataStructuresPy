import unittest
import numpy as np
from parameterized import parameterized
from dataStructures.linkedList import DoublyLinkedNode, DoublyLinkedList


class TestInitDoublyLinkedList(unittest.TestCase):
    @parameterized.expand([
        [None],
        ["hello"],
        [True],
    ])
    def testHandleNonArrayInputs(self, array):
        self.assertRaises(AssertionError, DoublyLinkedList, array)

    @parameterized.expand([
        [[1,2,6,10,4,111,9580]],
        [[1, True, 6, 10, False, None, 9580, "testing"]],
    ])
    def testHandleMultiDataTypedArrayInputs(self, array):
        self.assertTrue(isinstance(DoublyLinkedList(array=array), DoublyLinkedList))

    @parameterized.expand([
        [[1,2,6,10,4,111,9580]],
        [[1, True, 6, 10, False, "None", 9580]],
    ])
    def testAppendNode(self, array):
        #TODO
        dll = DoublyLinkedList(array=array)
        previousLastNode = dll.lastNode
        newNode = DoublyLinkedNode(value="testing")
        dll.append(newNode)
        self.assertEqual(dll.lastNode, newNode)
        self.assertEqual(previousLastNode, newNode.prev)
        self.assertEqual(previousLastNode.next, newNode)
        self.assertTrue(previousLastNode.hasNext())
        self.assertTrue(dll.lastNode.hasPrev())
        self.assertFalse(dll.lastNode.hasNext())
        
    def testAppendNoneNode(self):
        #TODO
        pass