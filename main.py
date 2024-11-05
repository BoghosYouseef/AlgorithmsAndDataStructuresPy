import logging
logging.basicConfig(level=logging.DEBUG)

from utils.pathHandling import getDataStructuresAbsPath
from dataStructures.linkedList import Node, DoublyLinkedList

if __name__ == "__main__":
    print("YO")
    list1 = [5, 10, 29, 2344, 23,11, 2, 0, 144]
    dll = DoublyLinkedList(array=list1)
    newNode = Node(value=829357)
    dll.append(newNode)
    pass