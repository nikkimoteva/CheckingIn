import NotificationAnnoyer

def main():
    # I want to ask if they've done the particular task
    task = raw_input("what did you do today? ")
    NotificationAnnoyer.ask(task)
    NotificationAnnoyer.another_task()
    print "ahhhh", task

if __name__ == '__main__':
    main()