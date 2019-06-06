import re


def switch(i, d, linky):
    if 0 <= i <= 5:
        switcher = {
            0: "ALERT! THE DEADLINE IS TODAY. YOU WILL MISS THE DEADLINE IF YOU DON'T FINISH THE TASK TODAY!",
            1: "URGENT!!! you have " + str(d) + " day left!!! This is an important task that needs"
                                                " to be done as soon as possible",
            2: "Kinda urgent! you have " + str(d) + " days left, but since this is a high level task, "
                                                    "I recommend doing it in the next few days",
            3: "you have " + str(d) + " days left. It's not very urgent now, "
                                      "but I think it's better to do it in the next " + str(time(d)) +
                                    " days to avoid unnecessary high stress levels",
            4: "you have " + str(d) + " days left. You can still manage to procrastinate based on the level of "
                                      "the task. I would recommend for you to work on tasks with higher urgency,"
                                      " such as: " + str(todo(d, linky)),
            5: "you have missed the deadline"
        }
        return switcher[i]
    else:
        print "invalid"


def give_recommend(d, s, linky):

    # NotSure.py #2

    # parsing the urgency of a task
    q = re.findall("\d*", s)
    q = int("".join(q))

    # If the task is important (HIGH LEVEL) and there are few days left
    if d >= 0:
        if d == 0:
            return switch(0, d, linky)
        elif d <= 2:
            return switch(1, d, linky)
        elif d <= 5 and q <= 5:
            return switch(2, d, linky)
        elif d <= 5:
            return switch(3, d, linky)
        else:
            return switch(4, d, linky)
    else:
        return switch(5, d, linky)


def todo(day, linky):
    l = linky.__len__()
    print l
    if l >= day:
        q = l - day + 1
    else:
        q = l
    for i in range(1, q):
        print i
        k = linky.print_k(i)
        if str(k) != "None":
            return k
        else:
            break


def time(day):
    x = day - (day * 0.16)
    return int(round(x))
