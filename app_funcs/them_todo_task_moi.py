from models.todo_task import TodoTask;
from data_helpers.save_file import SaveFile;
from data_helpers.read_file import ReadFile;

def ThemTodoTaskMoi(name, description):
    todoTaskMoi = TodoTask(name, description);

    todoTaskList = list(ReadFile());
    todoTaskList.append(todoTaskMoi);

    SaveFile(todoTaskList);
    
def NhapTodoTaskMoi():
    print("Nhap ten todo: ");
    todoName = input();
    print("Nhap mo ta todo: ");
    todoDescription = input();

    ThemTodoTaskMoi(todoName, todoDescription);
    print("Them todo moi thanh cong");
    input();