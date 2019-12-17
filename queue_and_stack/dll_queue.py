import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    """
    First-In-First-Out (FIFO)
    """

    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # Add an item to the back of the queue
        self.value = value
        self.size += 1
        self.storage.add_to_tail(self.value)

    def dequeue(self):
        # Remove and return an item from the front of the queue
        if self.size > 0:
            item = self.storage.remove_from_head()
            self.size -= 1
            return item
        else:
            return

    def len(self):
        # Returns the number of items in the queue
        return self.size
