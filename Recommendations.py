import NotificationAnnoyer
import TaskLL
import re


def main2(d, s):
    switcher = {
        0: "ALERT! THE DEADLINE IS TODAY. YOU WILL MISS THE DEADLINE IF YOU DON'T FINISH THE TASK TODAY!",
        1: "URGENT!!! you have " + str(d) + " day left!!! This is an important task that needs"
                                              " to be done as soon as possible",
        2: "Kinda urgent! you have " + str(
            d) + " days left, but since this is a high level task, I recommend doing it"
                   "in the next few days",
        3: "you have " + str(d) + " days left. It's not very urgent now, "
                                    "but I think it's better to do it in the next " + str(time(d))
           + " days to avoid unnecessary high stress levels",
        4: "you have " + str(d) + " days left. You can still manage to procrastinate based on the level of the task," \
                                    " I would recommend for you to work on tasks with higher urgency, such as: " + todo(),
        5: "you have missed the deadline"
    }
    print switcher.get(d, "invalid")
    # NotSure.py #2

    # parsing the urgency of a task
    q = re.findall("\d*", s)
    q = int("".join(q))
    print q

    # If the task is important (HIGH LEVEL) and there are few days left
    if d == 0:
        print switcher[0]
    elif d <= 2:
        print switcher[1]
    elif d <= 5 and q <= 5:
        print switcher[2]
    elif d <= 5:
        print switcher[3]
    elif d > 5:
        print switcher[4]
    else:
        print switcher[5]



def time(day):
    return "number place-holder"


def todo():
    return "place-holder"


if __name__ == "__main__":
    print main2(3, "task 2")
