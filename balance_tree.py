class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "red"  # Initially, all nodes are red

class RedBlackTree:
    ''' Red-Black Tree, Psudocode edition '''
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            # First node becomes the root and is colored black
            self.root = new_node
            new_node.color = "black"
            return
            
        # Regular binary search tree insertion
        current = self.root
        while True:
            if new_node.data < current.data:
                if not current.left:
                    current.left = new_node
                    new_node.parent = current
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    new_node.parent = current
                    break
                current = current.right
                
        # Fix the tree to maintain Red-Black properties
        self._balance_after_insert(new_node)

    def _balance_after_insert(self, node):
        # Balance the tree after insertion
        while node != self.root and node.parent.color == "red":
            # If parent is a left child of grandparent
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                
                # Case 1: Uncle is red
                if uncle and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    # Case 2: Node is a right child
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    
                    # Case 3: Node is a left child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_right(node.parent.parent)
            
            # If parent is a right child of grandparent (parent.parent)
            else:
                uncle = node.parent.parent.left
                
                # Case 1: Uncle is red
                if uncle and uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    # Case 2: Node is a left child
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    
                    # Case 3: Node is a right child
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_left(node.parent.parent)
                    
        # Ensure root is always black
        self.root.color = "black"

    def _rotate_left(self, node):
        # Perform a left rotation at 'node'
        right_child = node.right
        node.right = right_child.left
        
        if right_child.left:
            right_child.left.parent = node
            
        right_child.parent = node.parent
        
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
            
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        # Perform a right rotation at 'node'
        left_child = node.left
        node.left = left_child.right
        
        if left_child.right:
            left_child.right.parent = node
            
        left_child.parent = node.parent
        
        if not node.parent:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
            
        left_child.right = node
        node.parent = left_child

    def print_tree(self):
        self._print_tree_helper(self.root)

    def _print_tree_helper(self, node):
        if not node:
            return
        print(f"Node: {node.data}, Color: {node.color}")
        self._print_tree_helper(node.left)
        self._print_tree_helper(node.right)


# Example Usage:
tree = RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)

tree.print_tree()
