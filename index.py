from number_to_func import NumberToFunc;
import os;

def ClearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear');


def HienThiDanhSachChucNang():
    print("Nhap vao lua chon cua ban:");
    print("0: Thoat chuong trinh");
    print("1: Them Todo moi");
    print("2: Xoa Todo o vi tri la");
    print("3: Cap nhat Todo o vi tri");
    print("4: Hoan thanh Todo o vi tri");
    print("5: In toan bo Todo dang co");
    print("6: In toan bo Todo da hoan thanh");
    print("7: In toan bo Todo chua hoan thanh");

while(True):
    ClearConsole();
    HienThiDanhSachChucNang();
    # Nhap lua chon
    try:
        luaChon = int(input("Lua chon cua ban: "));
        if luaChon >= 0 and luaChon <= 7:
            luaChonFunc = NumberToFunc(luaChon);
            if luaChonFunc is not None:
                luaChonFunc();
            else:
                break;
        else:
            print("Lua chon chuc nang khong dung");
            input();
            continue
    except ValueError:
        print("Lua chon chuc nang khong dung");
        input();
        continue


print("Todo Console da thoat");