class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


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
