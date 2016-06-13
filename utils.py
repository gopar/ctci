class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def find_node(root, data):
    """
    Goes searching for node that contains given value.
    Returns either the node or None
    """
    if root is None:
        return None

    if root.data == data:
        return root

    if root.data > data:
        return find_node(root.left, data)
    return find_node(root.right, data)
