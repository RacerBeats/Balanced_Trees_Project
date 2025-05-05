class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = "red"  # all nodes are red


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.rotation_count = 0 # track rotations

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.root.color = "black"
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    break
                else:
                    current = current.right

        self._fix_insert(new_node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            parent = node.parent
            gp = parent.parent

            if parent == gp.left:
                uncle = gp.right

                if uncle and uncle.color == "red":
                    parent.color = "black"
                    uncle.color = "black"
                    gp.color = "red"
                    node = gp
                else:
                    if node == parent.right:
                        node = parent
                        self._rotate_left(node)
                    node.parent.color = "black"
                    gp.color = "red"
                    self._rotate_right(gp)
            else:
                uncle = gp.left

                if uncle and uncle.color == "red":
                    parent.color = "black"
                    uncle.color = "black"
                    gp.color = "red"
                    node = gp
                else:
                    if node == parent.left:
                        node = parent
                        self._rotate_right(node)
                    node.parent.color = "black"
                    gp.color = "red"
                    self._rotate_left(gp)

        self.root.color = "black"

    def _rotate_left(self, node):
        self.rotation_count += 1 #increment count
        right = node.right
        node.right = right.left
        if right.left is not None:
            right.left.parent = node
        right.parent = node.parent

        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right

        right.left = node
        node.parent = right

    def _rotate_right(self, node):
        self.rotation_count += 1 #increment count
        left = node.left
        node.left = left.right
        if left.right is not None:
            left.right.parent = node
        left.parent = node.parent

        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left

        left.right = node
        node.parent = left

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(f"{node.data} ({node.color})", end=" ")
            self.inorder(node.right)

    def print_tree(self, node, indent=""):
        if node is not None:
            print(indent + f"{node.data} ({node.color})")
            if node.left is not None or node.right is not None:
                if node.left:
                    self.print_tree(node.left, indent + "  ")
                else:
                    print(indent + "  " + "None")
                if node.right:
                    self.print_tree(node.right, indent + "  ")
                else:
                    print(indent + "  " + "None")

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return max(left_height, right_height) + 1


tree = RedBlackTree()
isbn_numbers = [
    1835,
    728,
    1491,
    377,
    1335,
    929,
    1120,
    45,
    311,
    1652,
    599,
    8,
    1442,
    135,
    1527,
    1221,
    516,
    110,
    634,
    966,
]

for num in isbn_numbers:
    tree.insert(num)
print("\n(Unsorted):")
print(isbn_numbers)
print("\n(Sorted):")
tree.inorder(tree.root)

print("\n\nTree Structure:")
tree.print_tree(tree.root)

# Print the height of the tree
print(f"\nTree Height: {tree.height(tree.root)}")
# Print the total number of rotations
print(f"Total Rotations: {tree.rotation_count}")