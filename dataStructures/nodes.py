from pdb import set_trace

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
    def __repr__(self):
        return f"Node({type(self.value)} {self.value})"

class DoublyLinkedNode(Node):
    def __init__(self, value):
        super().__init__(value)
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

        
class BinaryNode(Node):

    def __init__(self, value):
        super().__init__(value)
        self.right = None
        self.left = None
        self.parent = None
        self.count = 1
    

    def insert(self, _input):
        try:
            # set_trace()
            if not ( isinstance(_input, int) or isinstance(_input, float) or  isinstance(_input, str)):
                raise ValueError("The input must be a string, float or an int!")

            if _input > self.value:
                if self.right is None:
                    self.right = BinaryNode(value=_input)
                else:
                    self.right.insert(_input=_input)

            elif _input < self.value:
                if self.left is None:
                    self.left = BinaryNode(value=_input)
                else:
                    self.left.insert(_input=_input)

            else:
                self.count+=1
        except ValueError as e:
            raise