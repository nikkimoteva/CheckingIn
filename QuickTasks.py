import NotificationAnnoyer
import quick_storing
import Asker
import Data
#enter the tasks without including their data, just to remember them. Can edit them later

global quick_t
quick_t = []


def loading_tasks():
    global quick_t
    quick_t = quick_storing.load()
    print quick_t


def quick():
    print("Instructions: Please enter each task and press enter. To exit, enter the number -1")
    quick_tasks(quick_t)


def quick_tasks(quick_t):
    task = raw_input()
    if task != "-1":
        quick_t.append(task)
        quick_tasks(quick_t)
    else:
        Data.quick_dump(quick_t)
        Asker.main(0)

def entering_info_question():
    ans = raw_input("Please enter an option: \n"
                    "1. To enter the information of the current tasks \n"
                    "2. To enter new tasks \n"
                    "3. Go back to main page")
    if ans == "1":
        if not quick_t:
            print "the list is empty, please choose another option"
            entering_info_question()
        else:
            insert_info(quick_t)
    elif ans == "2":
        quick()
    elif ans == "3":
        Asker.main(0)
    else:
        print "please enter a valid option"
        entering_info_question()


# user wants to insert the information
def insert_info(quick_t):
    for i in quick_t:
        ans = raw_input("would you like to enter the info of the next task? (yes/no)")
        if ans == "yes":
            NotificationAnnoyer.add_task(i, "yes")
            quick_t.remove(i)
        else:
            Asker.main(0)