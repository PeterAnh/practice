class Node:
    def __init__(self, val, prev, next):
        self.index = val
        self.address = prev ^ next
    

class XORLinkedList:
    def __init__(self, root):
        self.root = Node()
    
    def add(self,element):
        current = self.root
        while(True):
            if(current.next_node == None):
                break
                
        new_node = Node(element,current)

        pass

    def get(index):
        pass

