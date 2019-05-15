import gc


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # insert in front of the Llist
    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        return new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print "the given previous node cannot be NULL"
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def delete_node(self, dele):
        if self.head is None or dele is None:
            return
        # deleting the head node
        if self.head == dele:
            self.head = dele.next
        # delete middle node
        if dele.next is not None:
            dele.next.prev = dele.prev
        # delete node that's not head
        if dele.prev is not None:
            dele.prev.next = dele.next
        gc.collect()

    def __len__(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def print_k(self, k):
        current = self.head
        p = k
        temp = current
        while p > 0:
            if temp is None:
                return None
            else:
                temp = temp.next
                p -= 1
        while temp is not None:
            temp = temp.next
            current = current.next
        return current.data


    def print_list(self):
        global last
        last = Node(None)
        n = self.head
        print "\nTraversal in forward direction"
        print "None"
        while n is not None:
            print n.data
            last = n
            n = n.next
        print "\nTraversal in reverse direction"
        while last is not None:
            print last.data
            last = last.prev


# test to see if linked list works
def main():
    d = DoublyLinkedList()
    p = Node(data="task3")
    d.insert("task0")
    d.insert("task1")
    d.insert("task2")
    d.insert("task3")
    d.insert("task4")
    d.insert("task9")
    print len(d)
    print d.print_k(2)
    print d.print_list()


if __name__ == "__main__":
    main()
