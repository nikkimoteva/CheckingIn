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


def open_it(data):
    node = linked_list.find_node(data)
    if node == None:
        print "please enter an existing task"
        NotificationAnnoyer.look_at_task()
    else:
        a = raw_input("would you like to see the content of this task?(yes/no) ")
        open_it_helper(data, a)


def open_it_helper(data, a):
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
        print temp.data + " : " + NotificationAnnoyer.tasks_dict[temp.data]["title"]
        go_through_helper(temp)
        temp = temp.next
    print "Those were all the tasks!"
    Asker.main()


def go_through_helper(linky):
    q = raw_input("would you like to check out the content of this task?(y/n) ")
    if q == "y":
        #print NotificationAnnoyer.tasks_dict[linky.data]
        print "\n"
        open_task(linky.data)
    elif q == "n":
        return
    else:
        print "please enter y or n"
        go_through_helper(linky)


def open_task(task):
    which = raw_input("please choose one of the options:\n"
                      "1. title\n"
                      "2. deadline\n"
                      "3. deadtime\n"
                      "4. start date\n"
                      "5. start time\n"
                      "6. time left\n"
                      "7. Recommendation\n"
                      "8. All\n"
                      "9. Go back\n")
    which = int(which)
    if which == 1:
        print switch(1, task)
    elif which == 2:
        print switch(2, task)
    elif which == 3:
        print switch(3, task)
    elif which == 4:
        print switch(4, task)
    elif which == 5:
        print switch(5, task)
    elif which == 6:
        print switch(6, task)
    elif which == 7:
        print switch(7, task)
    elif which == 8:
        open_it_helper(task, "yes")
    elif which == 9:
        option_go_back(task)
    else:
        print "invalid number, please enter one of the options"
        open_task(task)
    open_task_helper(task)


def open_task_helper(task):
    go = raw_input("would you like to go through another option?(y/n) ")
    if go == "y":
        open_task(task)
    else:
        print "okay, off to next task then\n"


def option_go_back(linky):
    node = linked_list.find_node(linky)
    ans = raw_input("go to previous task?(y/n) ")
    if ans == "y":
        if linky == linked_list.head.data:
            print "there are no tasks before " + str(linky)
            open_task(linky)
        else:
            go_to = node.prev
            print go_to.data
            go_through_helper(go_to)
    if ans == "no":
        open_task(linky)


def switch(n, task):
    switcher = {
        1: NotificationAnnoyer.tasks_dict[task]["title"],
        2: NotificationAnnoyer.tasks_dict[task]["deadline"],
        3: NotificationAnnoyer.tasks_dict[task]["deadtime"],
        4: NotificationAnnoyer.tasks_dict[task]["start date"],
        5: NotificationAnnoyer.tasks_dict[task]["start time"],
        6: NotificationAnnoyer.tasks_dict[task]["time left"],
        7: NotificationAnnoyer.tasks_dict[task]["Recommendation"]
    }
    return switcher[n]


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
    #print len(linked_list)
    #print linked_list.print_k(2)
    #print linked_list.print_list()
    #print p_k(2)
    #print random()
    #print redata_node("task0", "task9999")
    #print open_task("task1")


if __name__ == "__main__":
    main()
