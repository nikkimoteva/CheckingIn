import TaskLL
import random as r

linked_list = TaskLL.DoublyLinkedList()


def add_node(linky):
    if len(linked_list) == 0:
        linked_list.insert(linky.data)
    else:
        linked_list.append(linky.data)


def remove_node(linky):
    linked_list.delete_node(linky)


# opens up a random task
def random():
    c = r.randint(1, len(linked_list))
    print c
    linked_list.print_k(c)


# print the k first items
def p_k(k):
    temp = linked_list.head
    t = k
    while temp is not None and t > 0:
        print temp.data
        temp = temp.next
        t -= 1

# test to see if linked list works
def main():
    d = TaskLL.Node(data="task5")
    linked_list.insert("task0")
    linked_list.insert("task1")
    linked_list.insert("task2")
    linked_list.insert("task3")
    linked_list.insert("task4")
    linked_list.insert("task9")
    print len(linked_list)
    print linked_list.print_k(2)
    print linked_list.print_list()
    print p_k(2)
    print random()

    add_node(d)
    print linked_list.print_list()


if __name__ == "__main__":
    main()
