"""
Daily coding problem #3:
Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

Code author: Hoang Tuan Anh
Date: 10/09/2019
"""

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    string_tree = ""
    string_tree = string_tree + root.val + " "
    q = deque()
    q.append(root)

    while(q):
        s = q.popleft()
        if(s.left != None and s.right != None):
            q.append(s.left)
            q.append(s.right)
            string_tree = string_tree + s.left.val + " "
            string_tree = string_tree + s.right.val + " "
        elif(s.left != None):
            #If left child is null, add None to denote the left child vacancy in the tree
            q.append(s.left)
            string_tree = string_tree + s.left.val + " "
            string_tree = string_tree + "None" + " "
        elif(s.right != None):
            #If right child is null, add None to denote the right child vacancy in the tree
            q.append(s.right)
            string_tree = string_tree + "None" + " "
            string_tree = string_tree + s.right.val + " "
            

    return string_tree

def deserialize(s):

    #Turn string s into a list of values of nodes
    list_node = s.split(" ")[:-1]
    list_length = len(list_node)

    #Initialise node position
    current_node_pos = 0
    left_child_pos = current_node_pos + 1
    right_child_pos = left_child_pos + 1

    #Append the first node into the queue
    previousNode = Node(list_node[current_node_pos])
    q_node = deque()
    q_node.append(previousNode)
    left = True #This variable memorises whether we are adding left node or right node to tree

    while(q_node):
        s = q_node.popleft()
        loop_counter = 0

        #Loop only two times to add left and right children
        while(loop_counter != 2):

            if(left):
                if(left_child_pos < list_length and list_node[left_child_pos]):
                    s.left = Node(list_node[left_child_pos])
                    q_node.append(s.left)
                left_child_pos = left_child_pos + 2
                left = False
                loop_counter = loop_counter + 1
            else:
                if(right_child_pos < list_length and list_node[right_child_pos]):
                    s.right = Node(list_node[right_child_pos])
                    q_node.append(s.right)
                right_child_pos = right_child_pos + 2
                left = True
                loop_counter = loop_counter + 1
    
    return previousNode

def main():
    node = Node('root', Node('left', Node('left.left', Node('left.left.left'), Node('left.left.right')), ), Node('right', Node('right.left'), Node('right.right')))
    string_tree = serialize(node)
    print (string_tree)
    assert deserialize(serialize(node)).left.left.val == 'left.left'

if __name__ == '__main__':
    main()