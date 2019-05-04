import shelve

def initial_data():
    # tasks
    d = shelve.open('TODO', 'c')
    thistask = {
        "take a bath": "task1",
        "shower": "task2",
        "study": "task3",
        "cry": "task4"
      }
    d['tasks'] = thistask
    read_task()
    write_task(task)
    read_task()
    d.close()


def write_task(task):
    # need to append here instead of over-writing
    shelf = shelve.open('TODO', 'c')
    temp = shelf["tasks"]
    temp.update(task)
    shelf["tasks"] = temp
    shelf.close()
    read_task()

def read_task():
    shelf = shelve.open('TODO', 'r')
    for key in shelf.keys():
        #repr(key)
        print key, shelf[key]
        print key
        print shelf[key]
    shelf.close()
