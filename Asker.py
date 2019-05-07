import NotificationAnnoyer

def main():
    # I want to ask if they've done the particular task
    task = raw_input("please enter the name of a task: ")
    NotificationAnnoyer.ask(task)
    NotificationAnnoyer.another_task()
    print "tasks manipulated: ", task

if __name__ == '__main__':
    main()