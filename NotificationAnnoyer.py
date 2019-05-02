import datetime as dt
from django.utils.timezone import utc
import Asker
from datetime import datetime
import Data
# put in the tasks that need to be done
# input: subject, deadline

dateTime = dt.datetime.now().hour
print dateTime

# tasks
thistask = {
    "take a bath" : "task1",
    "shower" : "task2",
    "study" : "task3",
    "cry" : "task4"
    }
print thistask.items()


recommendation = "tomorrow"


starting_now = dt.datetime.utcnow().replace(tzinfo=utc)
startDate = starting_now.date()
startTime = starting_now.time()


def time_left():
    dDate = raw_input("When is the deadline (YYYY, MM, DD)? ")
    dTime = raw_input("When is the deadline (hours, minutes, seconds)? ")
    timeLeft = datetime.combine(dDate, dTime) - datetime.combine(startDate, startTime)
    # time = datetime.combine(deadlineDate, deadlineTime) - datetime.combine(startDate, startTime)
    print "time left: ", time_left
    return timeLeft

# NotSure.py


# send notification here
def ask(task):
    if dateTime == 11:
        done_yet(task)


# check if it's done
def done_yet(task_is_done):
    if task_is_done in thistask.keys():
        while 1:
            isDone = raw_input("have you finished the task(yes/no)? ")
            if isDone == "yes":
                print ("well done! you can now stop thinking about it")
                thistask.pop(task_is_done)
                print thistask
                break
            elif isDone == "no":
                print "You still have", '{} minutes, {} hours'.format(time_left().days, time_left().seconds), \
                    "left to do it. I recommend doing it by", recommendation
                break
            else:
                print "please enter either yes or no"
    else:
        print "This task is not in the list. Please add it to the list first"
        add = raw_input("Do you want to add " + task_is_done + " to the todo list? ")
        add_task(task_is_done, add)


def add_task(task, add):
    if add == "yes":
        value = "task" + raw_input("What level of urgency is " + task + "? ")
        if value in thistask.values():
            print "You already have a task in this level. Please enter a new level of urgency, or " \
                  "consider changing your urgency levels."
            x = raw_input("Please enter an option: 1. Change the urgency   2. Enter a new urgency ")
            if x == "2":
                add_task(task, "yes")
            elif x == "1":
                changing_urgency(task)
        else:
            time = time_left()
            thistask.update({task: value})
            print thistask
    else:
        print "Okay! I won't add it to your list then."
        print thistask


# changing the values in the dictionary
def changing_urgency(task):
    val = "task" + raw_input("which urgency level do you want to change?")
    print "levels in use: "
    print thistask.values()
    new = "task" + raw_input("to which level would you like to change it to?")
    if new in thistask.values():
        print "please enter a new level, this one is currently in use"
        changing_urgency(task)
    else:
        for key, value in thistask.items():
            print val
            if val == value:
                x = key
                thistask.pop(key)
                print x
                break
            else:
                continue
        thistask.update({x: new})
        print thistask
        add_task(task, "yes")


def another_task():
    y = raw_input("do you want to enter another task? ")
    if y == "yes":
        Asker.main()
    else:
        print "Okay. Well done on getting things accomplished today!"
