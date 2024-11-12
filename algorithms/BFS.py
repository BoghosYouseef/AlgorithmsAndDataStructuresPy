from dataStructures.nodes import BinaryNode

class BFS:

    @classmethod
    def find(cls, rootNode, element):
        try:
            _current_level_nodes = [rootNode]
            found = False
            if not isinstance(rootNode, BinaryNode):
                raise ValueError("Breadth First Search Aglorithm only works on BinaryNodes!")

            if rootNode.value == element:
                 return rootNode
            
            next_level_nodes = []

            while not found:
                for node in _current_level_nodes:
                    if isinstance(node, BinaryNode):
                        if node.value != element:
                            if node.left is not None:
                                next_level_nodes.append(node.left)
                            if node.right is not None:
                                next_level_nodes.append(node.right)
                        elif node.value == element:
                            return node
                    
                _current_level_nodes = next_level_nodes
                next_level_nodes = []
                if not _current_level_nodes:
                    return None
                
                
        except ValueError as e:
            raise