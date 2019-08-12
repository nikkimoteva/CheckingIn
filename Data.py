import os
import shelve
import contextlib
import NotificationAnnoyer
import pickle

pick = "pickle.dat"
quick_pick = "quick_pickle.dat"


def dump(tasks_todo):
    with open(pick, "wb") as f:
        pickle.dump(tasks_todo, f)

def quick_dump(quick_t):
    with open(quick_pick, "wb") as f:
        pickle.dump(quick_t, f)


def load():
    with open(pick, "rb") as f:
        pickle.load(f)

def quick_load():
    with open(quick_pick, "rb") as f:
        pickle.load(f)

# TODO use cPickle to save the keys as non-strings and their actual type


# task is string, the key of task_dict
def initial_data():
    # tasks
    text = "task-1"
    with contextlib.closing(shelve.open("TODO", 'c')) as shelf:
        shelf[text] = {
            "title": "pay rent",
            "deadline": "2019-05-20",
            "deadtime": "23:59:59",
            "start date": "2019-05-04",
            "start time": "15:45:57",
            "time left": NotificationAnnoyer.time_left("2019-05-20", "23:59:59"),
            "Recommendation": NotificationAnnoyer.Recommendations.give_recommend(
                NotificationAnnoyer.dead("2019-05-20", "23:59:59"), "task-1", NotificationAnnoyer.the_list)
        }
        shelf.close()
    initial = pickle.dumps(text)
    return initial



def write_task(task):
    # need to append here instead of over-writing
    with contextlib.closing(shelve.open('TODO', 'c', writeback=True)) as shelf:
        shelf[task] = NotificationAnnoyer.tasks_dict[task]
    pickle.dumps(task)


def load_pickle(task):
    return pickle.loads(task)

def read_task():
    with contextlib.closing(shelve.open("TODO", 'r')) as shelf:
        for key in shelf.keys():
            k = pickle.loads(key)
            print k, repr(shelf[key])


def delete_data(task):
    with contextlib.closing(shelve.open("TODO", 'c')) as shelf:
        try:
            del shelf[task]
        except KeyError:
            print "key does not exist in database"


def print_data():
    with contextlib.closing(shelve.open("TODO", 'r')) as shelf:
        for key, value in shelf.iteritems():
            print pickle.loads(key), repr(value)
    NotificationAnnoyer.another_task()
