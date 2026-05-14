from node import Node

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
            
    def _insert_recursive(self,current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                new_node = Node(value)
                current_node.left = new_node
                new_node.parent = current_node
            else:
                self._insert_recursive(current_node.left,value)
        else:
            if current_node.right is None:
                new_node = Node(value)
                current_node.right = new_node
                new_node.parent = current_node
            else:
                self._insert_recursive(current_node.right,value)
    
    def display_in_order(self,node):
        if node:
            self.display_in_order(node.left)
            print(node.value,end="-")
            self.display_in_order(node.right)
    
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """
        Visualizes the tree structure using indentation and prefixes.
        """
        if node is None and level == 0:
            node = self.root
            if node is None:
                print("Tree is empty.")
                return

        if node is not None:
            # Print the current node with indentation based on its depth
            print(" " * (level * 4) + prefix + str(node.value))
            
            # If children exist, recursively print them with labels
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

tree = BinaryTree()


for val in [10, 5, 15, 3, 7, 12, 18]:
    tree.insert(val)

print("Visual Tree Structure:")
tree.print_tree()

tree.display_in_order(tree.root)