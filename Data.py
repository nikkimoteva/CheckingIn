import shelve
import contextlib
import NotificationAnnoyer
import cPickle

# TODO use cPickle to save the keys as non-strings and their actual type


# task is string, the key of task_dict
def initial_data():
    # tasks
    with contextlib.closing(shelve.open("TODO", 'c')) as shelf:
        shelf["task-1"] = {
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


def write_task(task):
    # need to append here instead of over-writing
    with contextlib.closing(shelve.open('TODO', 'c', writeback=True)) as shelf:
        shelf[task] = NotificationAnnoyer.tasks_dict[task]


def read_task():
    with contextlib.closing(shelve.open("TODO", 'r')) as shelf:
        for key in shelf.keys():
            print repr(key), repr(shelf[key])


def delete_data(task):
    with contextlib.closing(shelve.open("TODO", 'c')) as shelf:
        try:
            del shelf[task]
        except KeyError:
            print "key does not exist in database"


def print_data():
    with contextlib.closing(shelve.open("TODO", 'r')) as shelf:
        for key, value in shelf.iteritems():
            print repr(key), repr(value)
    NotificationAnnoyer.another_task()
