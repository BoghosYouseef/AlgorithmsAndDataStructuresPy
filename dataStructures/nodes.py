class Node:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(repr(self))
    
    def __eq__(self, target):
        if not isinstance(target, Node):
            return NotImplemented
        else:
            firstCondition = self.value == target.value
            secondCondition = self.__hash__() == target.__hash__()
            if firstCondition and secondCondition:
                return True
            else:
                return False

class DoublyLinkedNode(Node):
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

        
    # def __eq__(self, target):
    #     if not isinstance(target, DoublyLinkedNode):
    #         return NotImplemented
    #     else:
    #         firstCondition = self.value == target.value
    #         secondCondition = self.__hash__() == target.__hash__()
    #         if firstCondition and secondCondition:
    #             return True
    #         else:
    #             return False