import TaskLL
import NotificationAnnoyer
import random as r
import Asker

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


def redata_node(old_data, new_data):
    temp = linked_list.head
    while temp is not None:
        if temp.data == old_data:
            temp.data = new_data
            return
        else:
            temp = temp.next
    linked_list.order()
    print "ERROR you shouldn't have reached here NotificationAnnoyer must have stopped you before"


def open_task(data):
    node = linked_list.find_node(data)
    if node == None:
        print "please enter an existing task"
        NotificationAnnoyer.look_at_task()
    else:
        a = raw_input("would you like to see the content of this task?(yes/no) ")
        if a == "yes":
            print NotificationAnnoyer.tasks_dict[data]
        elif a == "no":
            print "Okay, moving on then"
        else:
            print "please enter either yes or no"
            open_task(data)

def go_through():
    temp = linked_list.head
    while temp is not None:
        print temp.data
        go_through_helper(temp)
        temp = temp.next
    print "Those were all the tasks!"
    Asker.main()


def go_through_helper(linky):
    q = raw_input("would you like to check out the content of this task?(y/n) ")
    if q == "y":
        print NotificationAnnoyer.tasks_dict[linky.data]
        print "\n"
    elif q == "n":
        return
    else:
        print "please enter y or n"
        go_through_helper(linky)



# test to see if linked list works
def main():
    d = TaskLL.Node(data="task5")
    linked_list.insert("task0")
    linked_list.insert("task1")
    linked_list.insert("task2")
    linked_list.insert("task3")
    linked_list.insert("task4")
    linked_list.insert("task9")
    add_node(d)
    print len(linked_list)
    print linked_list.print_k(2)
    print linked_list.print_list()
    print p_k(2)
    print random()
    print redata_node("task0", "task9999")
    print open_task("task1")


if __name__ == "__main__":
    main()
