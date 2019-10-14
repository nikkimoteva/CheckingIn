import pytz
from tzlocal import get_localzone
import datetime
import Asker
from datetime import datetime as dt
import Recommendations
import LLFeatures
import re
import Data
import storing

# put in the tasks that need to be done
# input: subject, deadline

dateTime = datetime.datetime.now().hour
print dateTime



#NotSure.py #3



#print Recommendations.give_recommend(10, "task3")

# tasks
# To access element of a nested dictionary, we use indexing [] syntax in Python



# print(x.strftime("%A"))
# USE THIS FOR GETTING THE DAY OF THE WEEK!!!!


def deadline(dDates):
    year, month, day = map(int, dDates.split("-"))
    dDate = datetime.date(year, month, day)
    return dDate


def deadtime(dTimes):
    hours, minutes, seconds = map(int, dTimes.split(":"))
    dTime = datetime.time(hours, minutes, seconds)
    return dTime


def time_left(dDates, dTimes):
    starting = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
    starting_now = starting.astimezone(get_localzone())

    date_started = starting_now.date()
    y, m, d = date_started.year, date_started.month, date_started.day
    print y, m, d
    startDate = datetime.date(y, m, d)
    print startDate
    startTime = starting_now.time().replace(microsecond=0)

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


# print LLFeatures.linked_list.print_list()
the_list = LLFeatures.linked_list

# task_dict data: NotSure.py #5

global tasks_dict
tasks_dict = {}




def printing():
    for key, val in tasks_dict.iteritems():
        print key
        print tasks_dict[key]

#printing()
#print tasks_dict["task1"]
#print tasks_dict["task1"]["time left"]

# NotSure.py


# send alert here
def ask(task_title):
    if dateTime == 13:
        key_task(task_title)


def adding_dict():
    global tasks_dict
    tasks_dict = storing.load()
    printing()
    LLFeatures.re_do(tasks_dict)
    print LLFeatures.linked_list.print_list()


def key_task(task_title):
    for key in tasks_dict.keys():
        #t_id, t_val in tasks_dict.items():
        print key
        if tasks_dict[key]["title"] == task_title:
            task_id = key
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
                Data.delete_data(task_id)
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
            deadtime = raw_input("What time is the deadline (hh:mm:ss)? ")
            time_zone = starting.astimezone(get_localzone())
            startdate = time_zone.date()
            starttime = time_zone.time().replace(microsecond=0)
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
            Data.write_task(task_key)
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
                Data.delete_data(key)
                break
        tasks_dict.update({new: x})
        #Data.write_task(task)
        # Change the task name in LLFeatures here
        LLFeatures.redata_node(level, new)
        print LLFeatures.linked_list.print_list()
        add_task(task, "yes")


def look_at_task():
    ans = "task" + raw_input("please enter the number of the task you would like to take a look at: ")
    print ans
    LLFeatures.open_it(ans)


def another_task():
    y = raw_input("do you want to continue with the tasks?(yes/no) ")
    if y == "yes":
        Asker.main(0)
    elif y == "no":
        print "Okay. Well done on getting things accomplished today!"

