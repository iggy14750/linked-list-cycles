
""" In response to Mike Ressler's question of finding cycles in a linked list. """

class Node:
    """ The data structure to be used by my cycle-detecting methods. """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def build_list(iterable):
    """ Builds a list out of an iterable, in the same order as given. """
    head = None
    for item in reversed(iterable):
        head = Node(item, head)
    return head

def travel(node):
    """ A generator which acts as an iterator for my linked list. """
    while node is not None:
        data = node.data
        node = node.next
        yield data

def cycle1(head):
    """ The first implementation of cycle detector, linear space. """
    seen = set()
    while head is not None:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False

def cycle2(head):
    """ The second implementation, with constant space. """
    fast = head.next
    slow = head
    while fast and fast.next:
        if slow in (fast, fast.next):
            return True
        slow = slow.next
        fast = fast.next.next
    return False

if __name__ == '__main__':
    pass
