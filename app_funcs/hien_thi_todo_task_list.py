from models.todo_task import TodoTask;
from data_helpers.read_file import ReadFile;
from tabulate import tabulate;
from linqit import List;

def LoadToanBoTodoTaskList():
    todoTaskList = list(ReadFile());
    return todoTaskList;
    
def HienThiTodoTask(todoTaskList):
    print("Toan bo todo: ");
    
    headers = ["STT", "Ten todo", "Mo ta", "Hoan thanh"];
    
    # allRowData = [];

    # for i in range(0, len(todoTaskList)):
    #     todoTask = todoTaskList[i];
    #     rowData = [i+1, todoTask.name, todoTask.description, todoTask.isDone];
    #     allRowData.append(rowData);

    allRowData = List(enumerate(todoTaskList)).select(lambda args: [args[0] + 1, args[1].name, args[1].description, args[1].isDone]);
    
    print(tabulate(allRowData, headers));

    input();

# Hien thi toan bo todo
def HienThiToanBoTodoTask():
    toanBoTodoTaskList = LoadToanBoTodoTaskList();
    HienThiTodoTask(toanBoTodoTaskList);

# Chi hien thi todo da hoan thanh
def HienThiTodoTaskDaHoanThanh():
    toanBoTodoTaskList = List(LoadToanBoTodoTaskList());
    
    todoTaskListHienThi = toanBoTodoTaskList.where(lambda x: x.isDone);

    HienThiTodoTask(todoTaskListHienThi);

# Chi hien thi todo chua hoan thanh
def HienThiTodoTaskChuaHoanThanh():
    toanBoTodoTaskList = List(LoadToanBoTodoTaskList());

    todoTaskListHienThi = toanBoTodoTaskList.where(lambda x: not x.isDone);

    HienThiTodoTask(todoTaskListHienThi);