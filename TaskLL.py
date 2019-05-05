class DoublyLinkedList:
    class Node(object):
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

        def get_next(self):
            return self._next

        def __str__(self):
            return str(self._element)

    def __init__(self):
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):      # checks how many tasks are left to do
        return self._size

    def is_empty(self):     # check if all tasks are done and the list is empty
        return self._size == 0

    def inserting(self, element, predecessor, successor):
        new = self.Node(element, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new

    def deleting(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        if self._size == 0:
            return '[]'
        start = "["
        current_e = self._header.get_next()
        for i in range(self._size):
            start += str(current_e) + ", "
            current_e = current_e.get_next()

        return start[:-2] + ']'

    # Modifying list

    def first(self):
        if self.is_empty():
            raise Exception("Empty!")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Exception("Empty!")
        return self._trailer._prev._element

    def insert_first(self, e):
        self.inserting(e, self._header, self._header._next)

    def insert_last(self, e):
        self.inserting(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Exception("Empty!")
        return self.deleting(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("Empty!")
        return self.deleting(self._trailer._prev)


#Test to see if linked list works
def main():
    d = DoublyLinkedList()
    d.insert_first(1)
    print d.__str__()
    d.insert_last(2)
    d.insert_last(3)
    print d.__str__()


if __name__ == "__main__":
    main()
