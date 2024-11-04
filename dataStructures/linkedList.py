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
    
class DoublyLinkedList:

    def __init__(self, array: list):
        # TODO
        assert isinstance(array, list)

        self.content = []
        try:
            if len(array) <= 1:
                raise ValueError
            
            firstNode = Node(value=array[0])
            self.content.append(firstNode)
            
            for i in range(1,len(array)-1):
                newNode = Node(value=array[i])
                newNode.setPrev(self.content[i-1])
                self.content.append(newNode)
            
            lastNode = Node(value=array[-1])
            lastNode.setPrev(self.content[-2])
            self.content.append(lastNode)
            for i in range(len(self.content)-1):
                self.content[i].setNext(self.content[i+1])
      
        except ValueError as e:
            pass
        

    
    def __str__(self):
        representation = "".join([str(i.value)+" <=> " if i.hasNext() else str(i.value)+" -> None" for i in self.content])
        if self.content[0].hasPrev():
            representation = self.content[0].prev()+ " <=> " + representation
        else:
            representation = "None"+ " <- " + representation
        return representation