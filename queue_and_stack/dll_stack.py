import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Stack:
    """
    Last-In-First-Out (LIFO)
    """

    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Add an item to the top of the stack
        self.value = value
        self.size += 1
        self.storage.add_to_tail(self.value)

    def pop(self):
        # Remove and return an item from the top of the stack
        if self.size > 0:
            item = self.storage.remove_from_tail()
            self.size -= 1
            return item
        else:
            return

    def len(self):
        return self.size
