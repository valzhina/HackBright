# Linked list with Node/LinkedList classes


class Node:
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.adjacent = set()
        self.next = None

    def __repr__(self):
        return f"<Node {self.data}>"


class LinkedList:
    """Linked List using head and tail"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node_by_index(self, index):
        """Remove node with given index"""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None: # while current != 0
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

        >>> ll = LinkedList()
        >>> ll.add_node('dog')
        >>> ll.add_node('cat')
        >>> ll.add_node('fish')

        >>> ll.print_list()
        dog
        cat
        fish
        """

        current = self.head
        while current:
            print(current.data)
            current = current.next

    def get_node_by_index(self, idx):
        """Return a node with the given index::

        >>> ll = LinkedList()
        >>> ll.add_node('dog')
        >>> ll.add_node('cat')
        >>> ll.add_node('fish')

        >>> ll.get_node_by_index(0)
        <Node dog>

        >>> ll.get_node_by_index(2)
        <Node fish>

        >>> ll.get_node_by_index(4)
        Traceback (most recent call last):
        ...
        Exception: List not long enough
        """

        current = self.head
        for i in range(idx):
            if not current.next:
                raise Exception("List not long enough")
            current = current.next
        return current

def print_connected_nodes(node):
    """ Grapth aka linkedlist  """
    to_visit = []
    to_visit.append(node)

    seen = set()
    seen.add(node)

    while to_visit:
        current = to_visit.pop()
        print(current.data)
        print(current.adjacent)

        for i in current.adjacent:
            if i not in seen:
                to_visit.append(i)
                seen.add(i)

if __name__ == "__main__":
    import doctest

    # print
    # result = doctest.testmod()
    # if not result.failed:
    #     print("ALL TESTS PASSED. GOOD WORK!")
    # print

    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node.adjacent.add(node2)
    node2.adjacent.add(node)
    node2.adjacent.add(node3)
    node3.adjacent.add(node2)

    print_connected_nodes(node)

    # examples: to_visit[1]
    # 1-2
    # | \
    # 3  4 - 5
    # |
    # 6