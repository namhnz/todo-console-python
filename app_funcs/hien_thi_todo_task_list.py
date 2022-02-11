from models.todo_task import TodoTask;
from data_helpers.read_file import ReadFile;
from tabulate import tabulate;

def LoadToanBoTodoTaskList():
    todoTaskList = list(ReadFile());
    return todoTaskList;
    
def HienThiTodoTask(todoTaskList):
    print("Toan bo todo: ");
    
    headers = ["STT", "Ten todo", "Mo ta", "Hoan thanh"];
    
    allRowData = [];

    for i in range(0, len(todoTaskList)):
        todoTask = todoTaskList[i];
        rowData = [i+1, todoTask.name, todoTask.description, todoTask.isDone];
        allRowData.append(rowData);
    
    print(tabulate(allRowData, headers));

    input();

# Hien thi toan bo todo
def HienThiToanBoTodoTask():
    toanBoTodoTaskList = LoadToanBoTodoTaskList();
    HienThiTodoTask(toanBoTodoTaskList);

# Chi hien thi todo da hoan thanh
def HienThiTodoTaskDaHoanThanh():
    toanBoTodoTaskList = LoadToanBoTodoTaskList();

    todoTaskListHienThi = [];
    for i in range(0, len(toanBoTodoTaskList)):
        todoTask = toanBoTodoTaskList[i];
        if todoTask.isDone == True:
            todoTaskListHienThi.append(todoTask);

    HienThiTodoTask(todoTaskListHienThi);

# Chi hien thi todo chua hoan thanh
def HienThiTodoTaskChuaHoanThanh():
    toanBoTodoTaskList = LoadToanBoTodoTaskList();

    todoTaskListHienThi = [];
    for i in range(0, len(toanBoTodoTaskList)):
        todoTask = toanBoTodoTaskList[i];
        if todoTask.isDone == False:
            todoTaskListHienThi.append(todoTask);

    HienThiTodoTask(todoTaskListHienThi);