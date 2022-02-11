import pickle;

def ReadFile():
    try:
        with open("data/saved_todo_task_list.dat", "rb") as dataFile:
            todoTaskList = pickle.load(dataFile);
            return todoTaskList;
    except EOFError:
        todoTaskList = [];
        return todoTaskList;