import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import numpy as np

class Node:
    def __init__(self, value):
        self.value = value
        # self.position = 0
        self.prev = None
        self.next = None

    def setNext(self, next):
        self.next = next
    def setPrev(self, prev):
        self.prev = prev

    def hasNext(self):
        return self.next is not None
    
    def hasPrev(self):
        return self.prev is not None

    def __eq__(self, target):
        if not isinstance(target, Node):
            return NotImplemented

        else:
            firstCondition = self.value == target.value 
            secondCondition = self.__hash__() == target.__hash__()
            # if not (firstCondition and secondCondition):
            #     return False
            
            # currentSmallestUniqueChainSelf = [self.value]
            # currentSmallestUniqueChainTarget = [target.value]
 
            if firstCondition and secondCondition:
                return True
            else:
                return False

    def __hash__(self):
        return hash(repr(self))
        

class DoublyLinkedList:
    def __init__(self, array: list):
        # TODO
        try:
            assert isinstance(array, list) or isinstance(array, np.ndarray), "The input must be a list!"
            self._content = []
            self.firstNode, self.lastNode = None, None
            if len(array) <= 1:
                raise ValueError
            
            self.firstNode = Node(value=array[0])
            self._content.append(self.firstNode)
            
            for i in range(1,len(array)-1):
                newNode = Node(value=array[i])
                newNode.setPrev(self._content[i-1])
                self._content.append(newNode)
            
            self.lastNode = Node(value=array[-1])
            self.lastNode.setPrev(self._content[-2])
            self._content.append(self.lastNode)
            for i in range(len(self._content)-1):
                self._content[i].setNext(self._content[i+1])
      
        except ValueError:
            self._content = None
            logger.error("The list must contain at least two elements!")

        self.__check_if_none()

        del self._content

    def append(self, node):
        try:
            assert isinstance(node, Node), "Input is not a node!"
            currentNode = self.firstNode
            while currentNode.hasNext():
                currentNode = currentNode.next
            
            currentNode.setNext(node)
            node.setNext(None)
            node.setPrev(currentNode)
            self.lastNode = node
            logger.debug(f"Node with value {node.value} has been appended to the doubly linked list!")
            logger.debug(self)

        except ValueError:
            logger.error("The element to append must be of type (class) <Node>")


    def __check_if_none(self):
        assert self._content != None, "The DoublyLinkedList object was not instantiated correctly."
    
    def __str__(self):
        representation = "None <-"
        currentNode = self.firstNode
        while currentNode.hasNext():
            representation += " " + str(currentNode.value) + " <=>"
            currentNode = currentNode.next
        representation += " " + str(currentNode.value) + " -> None"
        return representation