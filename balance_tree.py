class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "red"  # Initially, all nodes are red

class RedBlackTree:
    ''' THIS IS THE PSUDOCODE VERSION OF THE RED BLACK TREE '''
    def __init__(self):
        self.NIL = Node(None)  # Sentinel node representing null children
        self.NIL.color = "black"
        self.root = self.NIL

    def insert(self, data):
        new_node = Node(data)
        self.root = self._insert_helper(new_node)
        self._fix_insert(new_node)  # Correct the tree after insertion


    def _insert_helper(self, node):
        if self.root == self.NIL:
            self.root = node
            return node

        current = self.root
        while True:
            if node.data < current.data:
                if current.left == self.NIL:
                    current.left = node
                    node.parent = current
                    return node
                else:
                    current = current.left
            else:
                if current.right == self.NIL:
                    current.right = node
                    node.parent = current
                    return node
                else:
                    current = current.right


    def _fix_insert(self, node):
        while node.parent and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
            else:
                uncle = node.parent.parent.left

            if uncle and uncle.color == "red":
                # Case 1: Uncle is red
                node.parent.color = "black"
                uncle.color = "black"
                node.parent.parent.color = "red"
                node = node.parent.parent  # Move up the tree
            else:
                # Case 2: Uncle is black
                if node == node.parent.right: # node is right child
                    node = node.parent
                    if node == node.parent.left:
                        # Case 2.1: Node is left child
                        # Perform a left rotation on the parent
                        self._rotate_left(node)
                    break # Exit loop after rotation
                else:
                    break # Exit loop since uncle is black and node is left child

            if node is None:
                break
        # Ensure root is always black
        self.root.color = "black"



    def _rotate_left(self, node):
        # Perform a left rotation at 'node'
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child



    def print_tree(self):
        self._print_tree_helper(self.root)

    def _print_tree_helper(self, node):
        if node is None or node == self.NIL:
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