from utils import TreeNode, ListNode, find_node


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
        root = TreeNode(array[middle])

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


def prob4_5(root):
    """
    Implement a function to check if a binary tree is a binary search tree
    """
    def is_tree_a_binary_search_tree(root, array=None):
        if array is None:
            array = []
        if root is None:
            return array

        array = is_tree_a_binary_search_tree(root.left, array)
        array.append(root.data)
        array = is_tree_a_binary_search_tree(root.right, array)
        return array

    array = is_tree_a_binary_search_tree(root)
    return array == sorted(array)


def prob4_8(T1, T2):
    """
    You have two very large binary trees: T1 with millions of nodes
    and T2 with hundreds of nodes. Create an algorithm to decide
    if T2 is a sub-tree of T1.
    """
    def is_subtree(T1, T2):
        # Empty tree is *always* subset of another tree
        if T2 is None:
            return True

        # We've gone through both trees and ended at same time, means it's same
        if T1 is None and T2 is None:
            return True

        # If either one finishes first, then it's not the same
        if T1 is None or T2 is None:
            return False

        return is_subtree(T1.left, T2.left) and is_subtree(T1.right, T2.right)

    subtree = find_node(T1, T2.data)
    # We couldn't find the node
    if not subtree:
        return False
    return is_subtree(subtree, T2)

if __name__ == '__main__':
    tree = TreeNode(5, TreeNode(1), TreeNode(10))
    root = TreeNode(100)
    root.left = tree
    another = TreeNode(5, TreeNode(1), TreeNode(10))

    print(find_node(root, 5))
