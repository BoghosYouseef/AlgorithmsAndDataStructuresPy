from utils.pathHandling import getDataStructuresAbsPath
from dataStructures.linkedList import DoublyLinkedList

if __name__ == "__main__":
    list1 = [5, 10, 29, 2344, 23,11, 2, 0, 144]
    dll = DoublyLinkedList(array=list1)
    dll = DoublyLinkedList(array="list1")
    print(dll)
    pass