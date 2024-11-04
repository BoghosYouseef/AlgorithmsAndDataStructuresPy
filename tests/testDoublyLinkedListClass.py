import unittest
import numpy as np
from parameterized import parameterized
from dataStructures.linkedList import DoublyLinkedList


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
