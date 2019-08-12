import pickle

pick = "quick_pickle.dat"

def dump(tasks_todo):
    with open(pick, "wb") as f:
        pickle.dump(tasks_todo, f)


def load():
    with open(pick, "rb") as f:
        return pickle.load(f)
