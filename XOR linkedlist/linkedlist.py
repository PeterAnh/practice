class Node:
    def __init__(self, val, prev, next):
        self.index = val
        self.address = prev ^ next

    def next_node(self, prev):
        next_node = self.address ^ prev
        return next_node
    
    def prev_node(self, next):
        prev_node = self.address ^ next
    

class XORLinkedList:
    def __init__(self, root):
        #Python does not support pointer, hence using the List structure to simulate pointer
        self.memory = [Node(None,-1,-1)]
    
    #Create root node
    def root(self):
        return 0, -1, self.memory[0]
    
    def add(self,element):
        current_index, previous_index, current = self.root()
        while(True):
            next_index = current.next_node(previous_index)
            if(next_index == -1):
                break
            previous_index = current_index
            current_index = next_index
            current = self.memory[next_index]

        new_node_index = len(self.memory)
        current_index = previous_index ^ new_node_index
        new_node = Node(element,current_index,-1)
        self.memory.append(new_node)

    def get(index):
        pass

