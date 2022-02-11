from app_funcs.them_todo_task_moi import NhapTodoTaskMoi;
from app_funcs.hien_thi_todo_task_list import HienThiToanBoTodoTask, HienThiTodoTaskDaHoanThanh, HienThiTodoTaskChuaHoanThanh;
from app_funcs.cap_nhat_todo_task import ChonCapNhatTodoTask, ChonHoanThanhTodoTask;
from app_funcs.xoa_todo_task import ChonXoaTodoTask;

def NumberToFunc(num):
    switcher = {
        0: None,
        1: NhapTodoTaskMoi,
        2: ChonXoaTodoTask,
        3: ChonCapNhatTodoTask,
        4: ChonHoanThanhTodoTask,
        5: HienThiToanBoTodoTask,
        6: HienThiTodoTaskDaHoanThanh,
        7: HienThiTodoTaskChuaHoanThanh
    }

    return switcher.get(num, "nothing");