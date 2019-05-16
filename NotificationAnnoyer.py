import pytz
from tzlocal import get_localzone
import datetime
import Asker
from datetime import datetime as dt
import Recommendations
import LLFeatures
import TaskLL
import re

# put in the tasks that need to be done
# input: subject, deadline

dateTime = datetime.datetime.now().hour
print dateTime

#NotSure.py #3

#print Recommendations.give_recommend(10, "task3")

# tasks
# To access element of a nested dictionary, we use indexing [] syntax in Python


def deadline(dDates):
    year, month, day = map(int, dDates.split("-"))
    dDate = datetime.date(year, month, day)
    return dDate


def deadtime(dTimes):
    hours, minutes, seconds = map(int, dTimes.split("-"))
    dTime = datetime.time(hours, minutes, seconds)
    return dTime


def time_left(dDates, dTimes):
    starting = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    starting_now = starting.astimezone(get_localzone())
    startDate = starting_now.date()
    startTime = starting_now.time()

    time = deadtime(dTimes)
    date = deadline(dDates)
    timeLeft = dt.combine(date, time) - dt.combine(startDate, startTime).replace(microsecond=0)
    if timeLeft.days < 0 and timeLeft.seconds <= 0:
        print "deadline has passed"
        pass
    else:
        return timeLeft


def dead(d, t):
    return time_left(d, t).days
LLFeatures.linked_list.insert("task1")
LLFeatures.linked_list.append("task30")
#print LLFeatures.linked_list.print_list()
the_list = LLFeatures.linked_list



tasks_dict = {
              "task1": {"title": "cancel Spotify premium",
                        "deadline": "2019-05-21",
                        "deadtime": "23-50-50",
                        "start date": "2019-05-05",
                        "start time": "14-57-09",
                        "time left": time_left("2019-05-21", "23-50-50"),
                        "Recommendation": Recommendations.give_recommend(dead("2019-05-21", "23-50-50"),
                                                                "task1", the_list)
                        },
              "task30": {"title": "pay rent",
                        "deadline": "2019-05-20",
                        "deadtime": "23-59-59",
                        "start date": "2019-05-04",
                        "start time": "15-45-57",
                        "time left": time_left("2019-05-20", "23-59-59"),
                        "Recommendation": Recommendations.give_recommend(dead("2019-05-20", "23-59-59"),
                                                                "task30", the_list)
                        }
              }



def printing():
    for key, val in tasks_dict.items():
        print tasks_dict[key]

#printing()
#print tasks_dict["task1"]
#print tasks_dict["task1"]["time left"]

# NotSure.py


# send alert here
def ask(task_title):
    if dateTime == 12:
        key_task(task_title)


def key_task(task_title):
    for t_id, t_val in tasks_dict.items():
        if tasks_dict[t_id]["title"] == task_title:
            task_id = t_id
            break
        else:
            task_id = ""
    done_yet(task_id, task_title)


# check if it's done
def done_yet(task_id, task_title):
    if task_id != "":
        while 1:
            isDone = raw_input("have you finished the task(yes/no)? ")
            if isDone == "yes":
                print ("well done! you can now stop thinking about it")
                # delete from dict
                tasks_dict.pop(task_id)
                print tasks_dict
                # remove task from LLFeatures
                #node = TaskLL.Node(data= task_id)
                LLFeatures.linked_list.delete_node(task_id)
                LLFeatures.linked_list.print_list()
                break
            elif isDone == "no":
                q = tasks_dict[task_id]["time left"]
                hours = q.seconds / 3600
                # get the deadline data, compute it without asking the user to enter it again, return
                print "You still have", '{} days, {} hours'.format(q.days,
                    hours), "left to do it.", tasks_dict[task_id]["Recommendation"]
                break
            else:
                print "please enter either yes or no"
    else:
        print "This task is not in the list. Please add it to the list first"
        add = raw_input("Do you want to add " + task_title + " to the todo list? ")
        add_task(task_title, add)


def add_task(task_title, add):
    if add == "yes":
        task_key = "task" + raw_input("What level of urgency is " + task_title + "? ")
        if task_key in tasks_dict.keys():
            print "You already have a task in this level. Please enter a new level of urgency, or " \
                  "consider changing your urgency levels."

            while 1:
                x = raw_input("Please enter an option: \n"
                              "1. Change " + task_key+"'s urgency \n"
                              "2. Enter a new urgency \n")
                if x == "2":
                    add_task(task_title, "yes")
                    break
                elif x == "1":
                    changing_urgency(task_title, task_key)
                    break
                else:
                    print "please enter either 1 or 2"
        else:
            # Add a new dictionary to tasks_dict
            starting = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
            title = task_title
            deadline = raw_input("When is the deadline (YYYY-MM-DD)? ")
            deadtime = raw_input("What time is the deadline (hours-minutes-seconds)? ")
            startdate = starting.astimezone(get_localzone()).date()
            starttime = starting.astimezone(get_localzone()).time()
            timeLeft = time_left(deadline, deadtime)
            recommend = Recommendations.give_recommend(dead(deadline, deadtime),
                                                       task_key, the_list)
            tasks_dict.update({task_key: {"title": title,
                                        "deadline": deadline,
                                        "deadtime": deadtime,
                                        "start date": startdate,
                                        "start time": starttime,
                                        "time left": timeLeft,
                                        "Recommendation": recommend},
                               })
            # add to LLFeature here
            LLFeatures.linked_list.append(task_key)
            print LLFeatures.linked_list.print_list()
            printing()
    else:
        print "Okay! I won't add it to your list then."
        printing()


# changing the values in the dictionary
def changing_urgency(task, level):
    x = []
    for key in tasks_dict.keys():
        q = re.findall("\d*", key)
        q = int("".join(q))
        x.append(q)
    print "levels in use: " + str(x)

    lvl = raw_input("to which level would you like to change it to? ")
    new = "task"+str(lvl)
    if new in tasks_dict.keys():
        print "please enter a new level, " + str(new) + " is currently in use"
        changing_urgency(task, level)

    # changing the level
    else:
        for key, value in tasks_dict.items():
            #title = tasks_dict[key]["title"]
            if key == level:
                x = value
                tasks_dict.pop(key)
                break
        tasks_dict.update({new: x})
        # Change the task name in LLFeatures here
        LLFeatures.redata_node(level, new)
        print LLFeatures.linked_list.print_list()
        add_task(task, "yes")


def look_at_task():
    ans = "task" + raw_input("please enter the number of the task you would like to take a look at: ")
    LLFeatures.open_it(ans)


def another_task():
    y = raw_input("do you want to enter another task?(yes/no) ")
    if y == "yes":
        Asker.main()
    elif y == "no":
        print "Okay. Well done on getting things accomplished today!"



