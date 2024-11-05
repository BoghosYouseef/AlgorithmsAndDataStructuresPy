import logging
logging.basicConfig(level=logging.DEBUG)

from pdb import set_trace

from utils.pathHandling import getDataStructuresAbsPath
from dataStructures.linkedList import DoublyLinkedNode, DoublyLinkedList

if __name__ == "__main__":
    print("YO")
    # list1 = [5, 10, 29, 2344, 23,11, 2, 0, 144]
    list1 = [1, 2, 1, 5, 1,2, 1, 0, 144]
    dll = DoublyLinkedList(array=list1)
    
    newNode = DoublyLinkedNode(value=829357)
    dll.append(newNode)
    pass