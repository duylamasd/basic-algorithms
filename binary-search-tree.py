import sys

MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize - 1


class Queue:
    """
    This class represents a queue
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Node:
    """
    This class represents a node in binary search tree
    """

    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value


class BinarySearchTree:
    """
    This class represents a binary search tree
    """

    def insert(self, root, node):
        if root.value > node.value:
            if root.left_child is None:
                root.left_child = node
            else:
                self.insert(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
            else:
                self.insert(root.right_child, node)

    def in_order_print(self, root):
        if not root:
            return

        self.in_order_print(root.left_child)
        print root.value
        self.in_order_print(root.right_child)

    def pre_order_print(self, root):
        if not root:
            return

        print root.value
        self.pre_order_print(root.left_child)
        self.pre_order_print(root.right_child)

    def post_order_place(self, root):
        if not root:
            return None

        self.post_order_place(root.left_child)
        self.post_order_place(root.right_child)
        print root.value


def is_bst(root, min, max):
    """
    Check if tree is BST
    """
    if not root:
        return True

    if root.value < min or root.value > max:
        return False

    return is_bst(root.left_child, min, root.value - 1) and is_bst(root.right_child, root.value + 1, max)


def count_nodes(root):
    """
    Number of nodes of the tree
    """
    if root is None:
        return 0

    return 1 + count_nodes(root.left_child) + count_nodes(root.right_child)


def is_complete(root, idx, number_of_nodes):
    """
    Check if tree is complete
    """
    if root is None:
        return True

    if idx >= number_of_nodes:
        return False

    return is_complete(root.left_child, 2 * idx + 1, number_of_nodes) and is_complete(root.right_child, 2 * idx + 2, number_of_nodes)


def level_order(root):
    """
    Traverses bst by level order.
    The same algorithm to BFS
    """
    if root is None:
        return

    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        current = queue.dequeue()
        print current.value

        if current.left_child is not None:
            queue.enqueue(current.left_child)
        if current.right_child is not None:
            queue.enqueue(current.right_child)


def lca(root, n1, n2):
    """
    Find the lowest common ancestor of n1 and n2.
    This function assumes both n1 and n2 are present in BST
    """

    if root is None:
        return None

    if root.value > n1 and root.value > n2:
        return lca(root.left_child, n1, n2)

    if root.value < n1 and root.value < n2:
        return lca(root.right_child, n1, n2)

    return root


def iterative_lca(root, n1, n2):
    while root is not None:
        if root.value > n1 and root.value > n2:
            root = root.left_child
        elif root.value < n1 and root.value < n2:
            root = root.right_child
        else:
            break

    return root


root = Node(5)
bst = BinarySearchTree()
bst.insert(root, Node(2))
bst.insert(root, Node(8))
bst.insert(root, Node(1))
bst.insert(root, Node(4))
bst.insert(root, Node(6))
bst.insert(root, Node(9))

# bst.post_order_place(root)
print is_bst(root, MIN_INT, MAX_INT)

number_of_nodes = count_nodes(root)
print is_complete(root, 0, number_of_nodes)

level_order(root)

print lca(root, 6, 9).value
print iterative_lca(root, 6, 9).value
