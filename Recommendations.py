import NotificationAnnoyer
import TaskLL
import re


def main2(d, s):
    temp = TaskLL.DoublyLinkedList()
    # Number of days left
    temp.insert_first("less than 1 day")
    if d >= 1:
        temp.insert_last(" 1 day")
    for i in range(2, d+1):
        temp.insert_last(str(i) + " days")
    print temp.__str__()

    # parsing the urgency of a task
    q = re.findall("\d*", s)
    q = "".join(q)
    print q

    # If the task is important (HIGH LEVEL) and there are few days left
    if d <= 2:
        recommendation(1, d)
    elif d <= 5 and q <= 5:
        recommendation(2, d)
    elif d <= 5:
        recommendation(3, d)
    else:
        recommendation(4, d)


#
def recommendation(d, day):
    switcher = {
        1: "URGENT!!! you have "+ str(day) + " day left!!! This is an important task that needs"
                                             " to be done as soon as possible",
        2: "Kinda urgent! you have "+ str(day) + " days left, but since this is a high level task, I recommend doing it"
                                               "in the next few days",
        3: "you have " + str(day) + " days left. It's not very urgent now, "
                                   "but I think it's better to do it in the next "+ str(time(day))
           + " days to avoid unnecessary high stress levels",
        4: "you have " + str(day) + " days left. You can still manage to procrastinate based on the level of the task," \
                                 " I would recommend for you to work on tasks with higher urgency, such as: " + todo()
    }
    print switcher.get(d, "invalid")


def time(day):
    return -1


def todo():
    return "place-holder"


if __name__ == "__main__":
    main2(3, "task 2")
