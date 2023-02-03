"""

Author: Anders Mouanga (salticecream)
Description: AVL tree implementation in Python

"""

class Node:
    def __init__ (self, val):
        self.val = val
        if self.val == None:
            return
        self.left = Node(None)
        self.right = Node(None)
        self.height = 1 

class Tree:
    def __init__(self, val):
        self.root = Node(val)
        self.nodes = [self.root]
    
    def insert(self, val, current_node = "Default"):
        # set the default node for this function to the root
        if current_node == "Default":
            current_node = self.root
    
        if current_node.val:
            if val > current_node.val:
                # check to see if we have reached the bottom
                if not current_node.right.val:
                    current_node.right = Node(val)
                    self.nodes.append(Node(val))
                    return
                else:
                    self.insert(val, current_node.right)
            
            elif val < current_node.val:
                # check to see if we have reached the bottom
                if not current_node.left.val:
                    current_node.left = Node(val)
                    self.nodes.append(Node(val))
                    return
                else:
                    self.insert(val, current_node.left)
            
            else:   # val = current_node
                pass
    
    # print the path to the specified node
    def find(self, val, node = "Default", nodes_traversed = []):
        # set default argument
        if node == "Default":
            node = self.root
        
        
        if val > node.val:
            self.find(val, node.right, nodes_traversed + [node.val])
        
        elif val < node.val:
            self.find(val, node.left, nodes_traversed + [node.val])
        
        else:   # val = node.val
            return nodes_traversed

        
    
    def print(self):
        for node in self.nodes:
            print(f"Node `{node.val}` has left node: {node.left.val} and right node: {node.right.val}")
        

# test

# create a tree with some values, including duplicate values, and print them all. also test print function
def test():
    tree = Tree(10)
    tree.insert(5)
    tree.insert(5)
    tree.insert(15)
    tree.insert(5)

    print("To find 5, we go through",tree.find(5))
    tree.print()



test()
