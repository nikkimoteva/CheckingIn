import NotificationAnnoyer
import TaskLL
import re


def switch(i, d):
    if 0 <= i <= 5:
        switcher = {
            0: "ALERT! THE DEADLINE IS TODAY. YOU WILL MISS THE DEADLINE IF YOU DON'T FINISH THE TASK TODAY!",
            1: "URGENT!!! you have " + str(d) + " day left!!! This is an important task that needs"
                                                " to be done as soon as possible",
            2: "Kinda urgent! you have " + str(d) + " days left, but since this is a high level task, "
                                                    "I recommend doing it in the next few days",
            3: "you have " + str(d) + " days left. It's not very urgent now, "
                                      "but I think it's better to do it in the next " \
               + " days to avoid unnecessary high stress levels",
            4: "you have " + str(d) + " days left. You can still manage to procrastinate based on the level of the task," \
                                      " I would recommend for you to work on tasks with higher urgency, such as: ",
            5: "you have missed the deadline"
        }
        return switcher[i]
    else:
        print "invalid"


def give_recommend(d, s):

    # NotSure.py #2

    # parsing the urgency of a task
    q = re.findall("\d*", s)
    q = int("".join(q))

    # If the task is important (HIGH LEVEL) and there are few days left
    if d == 0:
        return switch(0, d)
    elif d <= 2:
        return switch(1, d)
    elif d <= 5 and q <= 5:
        return switch(2, d)
    elif d <= 5:
        return switch(3, d)
    elif d > 5:
        return switch(4, d)
    else:
        return switch(5, d)



def time(day):
    print "number place-holder"


def todo():
    print "place-holder"
