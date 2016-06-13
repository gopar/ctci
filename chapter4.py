class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def prob4_1(root):
    """
    Implement a function to check if a binary tree is balanced.
    Height of two subtrees of any node never differ by more than one.
    """
    def isBalanced(root):
        if root is None:
            return 0
        left = isBalanced(root.left)
        right = isBalanced(root.right)
        if left < 0 or right < 0 or abs(left-right) > 1:
            return -1
        return max(left, right) + 1

    return isBalanced(root) >= 0


def prob4_2():
    """
    Given a directed Graph, design an algorithm to find out whether there is a
    route between two nodes.
    """
    def find_route(graph, start, end, path=None):
        path = (path or []) + [start]

        if start == end:
            return path

        for node in graph.get(start, []):
            if node not in path:
                new_path = find_route(graph, node, end, path)
                if new_path:
                    return new_path
        return None

    return find_route


def prob4_3():
    """
    Given a sorted (increasing order) array, write an algorithm to create
    a binary search tree with minimal height.
    """
    def create_binary_search_tree(array, start, end):
        if end < start:
            return None
        middle = (start + end) // 2
        root = Node(array[middle])

        root.left = create_binary_search_tree(array, start, middle - 1)
        root.right = create_binary_search_tree(array, middle + 1, end)

        return root

    return create_binary_search_tree


def prob4_4():
    """
    Given a binary tree, design an algorithm which creates a linked list of
    all the nodes at each depth.
    (ex: If you have depth D, then you had D linked lists)
    """
    def binary_tree_to_linked_list(root, level=0, array=[]):
        if root is None:
            return array

        try:
            array[level].next = ListNode(root.data)
        except IndexError:
            array.append(ListNode(root.data))

        array = binary_tree_to_linked_list(root.left, level + 1, array)
        array = binary_tree_to_linked_list(root.right, level + 1, array)

        return array
    return binary_tree_to_linked_list

if __name__ == '__main__':
    tree = Node('A', Node('B'), Node('C'))
    result = prob4_4()(tree)

    for node in result:
        root = node
        while root is not None:
            print('Data: ' + root.data)
            root = root.next
