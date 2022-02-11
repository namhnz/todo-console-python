import pickle;

def SaveFile(todoTaskList):
    with open("data/saved_todo_task_list.dat", "wb") as dataFile:
        pickle.dump(todoTaskList, dataFile);