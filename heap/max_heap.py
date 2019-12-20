class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        """
        Adds the input value into the heap; 
        this method should ensure that the inserted 
        value is in the correct spot in the heap
        """
        if self.storage:
            self.storage.append(value)
            self._bubble_up(self.get_size()-1)
        else:
            self.storage.append(value)

    def delete(self):
        """
        Removes and returns the 'topmost' value 
        from the heap; this method needs to ensure 
        that the heap property is maintained after 
        the topmost element has been removed.
        """
        if self.storage:
            top = self.storage[0]
            self.storage[0] = self.storage[-1]
            self.storage = self.storage[:-1]
            self._sift_down(0)
            return top
        else:
            return

    def get_max(self):
        """
        Returns the maximum value in the heap in constant time.
        """
        return self.storage[0]

    def get_size(self):
        """
        Returns the number of elements stored in the heap.
        """
        return len(self.storage)

    def _bubble_up(self, index):
        """
        Moves the element at the specified index "up" 
        the heap by swapping it with its parent if 
        the parent's value is less than the value 
        at the specified index.
        """
        # Right
        if index % 2 == 0 and index > 0:
            parent = (index - 2) // 2
            if self.storage[parent] < self.storage[index]:
                self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
                self._bubble_up(parent)
        # Left
        elif index % 2 == 1:
            parent = (index - 1) // 2
            if self.storage[parent] < self.storage[index]:
                self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
                self._bubble_up(parent)
        else:
            return

    def _sift_down(self, index):
        """
        Grabs the indices of this element's children 
        and determines which child has a larger value. 
        If the larger child's value is larger than the 
        parent's value, the child element is swapped 
        with the parent.
        """
        l_child = index * 2 + 1
        r_child = index * 2 + 2
        if l_child and r_child <= self.get_size() - 1:
            if self.storage[l_child] > self.storage[r_child]:
                if self.storage[l_child] > self.storage[index]:
                    self.storage[l_child], self.storage[index] = self.storage[index], self.storage[l_child]
                    self._sift_down(l_child)
            else:
                if self.storage[r_child] > self.storage[index]:
                    self.storage[r_child], self.storage[index] = self.storage[index], self.storage[r_child]
                    self._sift_down(r_child)
        elif l_child <= self.get_size() - 1:
            if self.storage[l_child] > self.storage[index]:
                self.storage[l_child], self.storage[index] = self.storage[index], self.storage[l_child]
                self._sift_down(l_child)
        elif r_child <= self.get_size() - 1:
            if self.storage[r_child] > self.storage[index]:
                self.storage[r_child], self.storage[index] = self.storage[index], self.storage[r_child]
                self._sift_down(r_child)
        else:
            return
