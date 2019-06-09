import NotificationAnnoyer
import LLFeatures
import Data

def main():
    # I want to ask if they've done the particular task
    ans = raw_input("please select an option:\n"
                    "1. entering a task\n"
                    "2. taking a look at a task\n"
                    "3. flip through tasks\n"
                    "4. exit\n")
    if ans == "1":
        task = raw_input("please enter the title of a task: ")
        NotificationAnnoyer.ask(task)
        NotificationAnnoyer.another_task()
        print "tasks manipulated: ", task
    elif ans == "2":
        NotificationAnnoyer.look_at_task()
    elif ans == "3":
        LLFeatures.go_through()
    elif ans == "4":
        Data.dump(NotificationAnnoyer.tasks_dict)
        return
    elif ans == "5":
        #Data.print_data()
        Data.initial_data()
        NotificationAnnoyer.adding_dict()
    else:
        print "\nplease enter one of the available options"
        main()


if __name__ == '__main__':
    main()