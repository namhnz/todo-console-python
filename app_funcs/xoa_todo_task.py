from data_helpers.read_file import ReadFile;
from data_helpers.save_file import SaveFile;
from app_funcs.hien_thi_todo_task_list import LoadToanBoTodoTaskList;

# Cap nhat todo
def ChonXoaTodoTask():
    print("Xoa todo o vi tri: ");

    sttTodoTaskXoa = int(input());
    
    toanBoTodoTaskList = LoadToanBoTodoTaskList();

    if sttTodoTaskXoa <= 0 or sttTodoTaskXoa > len(toanBoTodoTaskList):
        print("Vi tri todo can xoa khong dung");
        input();
        return;

    todoTaskXoa = toanBoTodoTaskList[sttTodoTaskXoa - 1];

    toanBoTodoTaskList.remove(todoTaskXoa);
    
    SaveFile(toanBoTodoTaskList);
    
    print("Xoa todo co STT la %d thanh cong" % sttTodoTaskXoa);

    input();
