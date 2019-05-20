import gc
import re


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
        #self.order()
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
        self.order()
        return

    def delete_node(self, delete):
        to_delete = self.find_node(delete)
        temp = self.head
        # base case
        if self.head is None or to_delete is None:
            return
        # delete head node
        if self.head == to_delete:
            self.head = to_delete.next
        # delete last node
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        # delete middle node
        if to_delete.next is not None:
            to_delete.next.prev = to_delete.prev
        if to_delete.prev is not None:
            to_delete.prev.next = to_delete.next
        # free the memory
        gc.collect()
        # return
        return self

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

    def find_node(self, data_string):
        temp = self.head
        while temp is not None:
            if temp.data == data_string:
                return temp
            temp = temp.next
        print "No such node has been found"

# dll order
    def order(self):
        # NotSure.py 4
        temp = self.head
        cur = self.head
        ordered = []
        while temp is not None:
            q = re.findall("\d*", temp.data)
            p = "".join(q)
            ordered.append(p)
            temp = temp.next
        ordered_list = sorted(ordered)
        i = 0
        while cur is not None:
            cur.data = "task" + ordered_list[i]
            i += 1
            cur = cur.next
        print self.print_list()
        return self

    def print_list(self):
        global last
        last = Node(None)
        n = self.head
        print "\nTraversal in forward direction"
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
    d.append("task4")
    d.append("task2")
    d.append("task1")
    d.append("task3")
    d.append("task9")
    d.order()
    #print len(d)
    #print d.print_k(2)
    print d.print_list()


if __name__ == "__main__":
    main()
