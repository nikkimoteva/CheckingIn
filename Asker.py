import NotificationAnnoyer
import LLFeatures
import Data
import QuickTasks

def main(arg):
    # I want to ask if they've done the particular task
    if arg == 1:
        NotificationAnnoyer.adding_dict()
        main(0)
    else:
        ans = raw_input("please select an option:\n"
                        "1. entering a task\n"
                        "2. taking a look at a task\n"
                        "3. flip through tasks\n"
                        "4. quick tasks\n"
                        "5. exit\n")
        if ans == "1":
            task = raw_input("please enter the title of a task: ")
            NotificationAnnoyer.ask(task)
            Data.dump(NotificationAnnoyer.tasks_dict)
            NotificationAnnoyer.another_task()
            print "tasks manipulated: ", task
        elif ans == "2":
            NotificationAnnoyer.look_at_task()
        elif ans == "3":
            LLFeatures.go_through()
            return
        elif ans == "4":
            try:
                QuickTasks.loading_tasks()
                QuickTasks.entering_info_question()
            except:
                print "except here"
                QuickTasks.quick()
        elif ans == "5":
            Data.dump(NotificationAnnoyer.tasks_dict)
            Data.quick_dump(QuickTasks.quick_t)
        else:
            print "\nplease enter one of the available options"
            main()


if __name__ == '__main__':
    main(1)