from data_helpers.read_file import ReadFile;
from data_helpers.save_file import SaveFile;
from app_funcs.hien_thi_todo_task_list import LoadToanBoTodoTaskList;

# Cap nhat todo
def ChonCapNhatTodoTask():
    print("Cap nhat todo o vi tri: ");

    sttTodoTaskCapNhat = int(input());

    toanBoTodoTaskList = LoadToanBoTodoTaskList();

    if sttTodoTaskCapNhat <= 0 or sttTodoTaskCapNhat > len(toanBoTodoTaskList):
        print("Vi tri todo can cap nhat khong dung");
        input();
        return;

    todoTaskChinhSua = toanBoTodoTaskList[sttTodoTaskCapNhat - 1];

    print("Nhap ten todo moi: ");
    todoTaskChinhSua.name = input();
    print("Nhap mo ta todo moi: ");
    todoTaskChinhSua.description = input();
    print("Todo da hoan thanh chua? (y/n): ");
    daHoanThanhInputResult = input();
    if daHoanThanhInputResult == "y":
        todoTaskChinhSua.isDone = True;
    else:
        todoTaskChinhSua.isDone = False;

    SaveFile(toanBoTodoTaskList);
    
    print("Cap nhat todo co STT la %d thanh cong" % sttTodoTaskCapNhat);

    input();

# Hoan thanh todo
def ChonHoanThanhTodoTask():
    print("Hoan thanh todo o vi tri: ");

    sttTodoTaskHoanThanh = int(input());
    
    toanBoTodoTaskList = LoadToanBoTodoTaskList();

    if sttTodoTaskCapNhat <= 0 or sttTodoTaskCapNhat > len(toanBoTodoTaskList):
        print("Vi tri todo can cap nhat khong dung");
        input();
        return;

    todoTaskHoanThanh = toanBoTodoTaskList[sttTodoTaskHoanThanh - 1];
    todoTaskHoanThanh.isDone = True;

    SaveFile(toanBoTodoTaskList);
    
    print("Hoan thanh todo co STT la %d thanh cong" % sttTodoTaskHoanThanh);

    input();