"""

Author: Anders Mouanga (salticecream)
Description: AVL tree implementation in Python

"""

class Node:
    def __init__ (self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1 

class Tree:
    def __init__(self, val):
        self.root = Node(val)
    
    def insert(self, val, current_node = "Default"):
        # set the default node for this function to the root
        if current_node == "Default":
            current_node = self.root
    
        
        if val > current_node:
            
            # check to see if we have reached the bottom
            if not current_node.right:
                current_node.right = val
                return
            else:
                self.insert(val, self.root.right)
        
        elif val < current_node:
            # check to see if we have reached the bottom
            if not current_node.left:
                current_node.left = val
                return
            else:
                self.insert(val, self.root.left)
        
        else:   # val = current_node
            pass



