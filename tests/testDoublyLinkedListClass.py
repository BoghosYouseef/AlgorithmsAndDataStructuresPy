import unittest
import numpy as np
from pdb import set_trace
from parameterized import parameterized
from dataStructures.nodes import Node,DoublyLinkedNode
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

    @parameterized.expand([
        [[1,2,6,10,4,111,9580]],
        [[1, True, 6, 10, False, "None", 9580]],
    ])
    def testAppendNode(self, array):
        dll = DoublyLinkedList(array=array)
        previousLastNode = dll.lastNode
        newNode = DoublyLinkedNode(value="testing")
        dll.append(newNode)

        self.assertIsInstance(newNode, Node)
        self.assertEqual(dll.lastNode, newNode)
        self.assertEqual(previousLastNode, newNode.prev)
        self.assertEqual(previousLastNode.next, newNode)
        self.assertTrue(previousLastNode.hasNext())
        self.assertTrue(dll.lastNode.hasPrev())
        self.assertFalse(dll.lastNode.hasNext())
        
    def testAppendNoneNode(self):
        dll = DoublyLinkedList(array=[1,2,6,10,4,111,9580])
        self.assertRaises(ValueError, dll.append, 1)
        self.assertRaisesRegex(ValueError,r"^Input \[<class 'int'>: 1\] is not a node!$", dll.append, 1)
        self.assertRaisesRegex(ValueError,r"^Input \[<class 'str'>: 1\] is not a node!$", dll.append, "1")
        self.assertRaisesRegex(ValueError,r"^Input \[<class 'str'>: \] is not a node!$", dll.append, "")
        self.assertRaisesRegex(ValueError,r"^Input \[<class 'NoneType'>: None\] is not a node!$", dll.append, None)
        self.assertRaisesRegex(ValueError,r"^Input \[<class 'dataStructures.nodes.Node'>: Node\(<class 'str'> None\)\] is not a node!$", dll.append, Node("None"))