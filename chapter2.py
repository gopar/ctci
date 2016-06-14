from utils import ListNode


def prob2_1(root):
    """
    Write code to remove duplicates from an unsorted linked list.
    """
    node = root
    _dict = {node.data: node.data}

    while node.next is not None:
        _next = node.next
        if _next.data in _dict:
            node.next = _next.next
        else:
            _dict[_next.data] = _next.data
        node = node.next

    return root


def prob2_2(root, k):
    """
    Implement an algorithm to find the kth to last element of a singly
    linked list.
    """
    # Assuming k is never greater than list size
    nodes = [root]
    node = root

    while node.next is not None:
        node = node.next
        nodes.append(node)

    return nodes[-k]


def prob2_3(node):
    """
    Implement an algorithm to delete a node in the middle of a singly linked
    list, given only access to that node

    Ex:
    input: Node 'c' from: a->b->c->d->e
    Result: a->b->d->e
    """
    if node is None or node.next is None:
        return None
    # Transform current node to node next to it
    node.data = node.next.data
    node.next = node.next.next
    return node


def prob2_4(node, number):
    """
    Write code to partition a linked list around a value x, such that all nodes
    less than x come before all nodes greater than or equal to x.
    """
    # I'm just going to order the nodes
    nodes = []

    while node is not None:
        nodes.append(node)
        node = node.next

    if nodes == []:
        return None
    nodes = sorted(nodes, key=lambda node: node.data)

    for i in range(len(nodes) - 1):
        node = nodes[i]
        node.next = nodes[i + 1]

    node = nodes[-1]
    node.next = None

    return nodes[0]


def prob2_5(n1, n2):
    """
    You have two numbers represented by a linked list, where each node contains
    a sigle digit. The digits are stored in reverse order, such that the 1's
    digit is at the head of the list. Write a function that adds the two numbers
    and returns the sum as a linked list.

    Ex:
    input: (7->1->6) + (5->9->2) = 617 + 295
    ouptut: 2->1->9 = 912
    """
    left = []
    right = []

    degree = 0
    while n1 is not None:
        left.append(n1.data * (10 ** degree))
        degree += 1
        n1 = n1.next

    degree = 0
    while n2 is not None:
        right.append(n2.data * (10 ** degree))
        degree += 1
        n2 = n2.next

    answer = sum(left) + sum(right)
    if len(left) == len(right) == 0:
        return None

    final = []
    while answer:
        tmp = answer % 10
        final.append(tmp)
        answer = answer // 10

    root = ListNode(final.pop(0))
    node = root
    while final:
        node.next = ListNode(final.pop(0))
        node = node.next

    return root
