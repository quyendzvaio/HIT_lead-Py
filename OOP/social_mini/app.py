from managers.user_manager import UserManager
from managers.auth_system import AuthSystem
from untils.security import SecurityHelper

class App:
    def __init__(self):
        self.user_manager = UserManager()
        self.security = SecurityHelper()
        self.auth = AuthSystem(self.user_manager, self.security)
        self.current_id = None
        
    def run(self):
        while True:
            self.show_menu()
            choice = input("Chon tac vu: ").strip()
            if choice == "1":
                self.handle_register()
            elif choice == "2":
                self.handle_login()
            elif choice == "3":
                self.handle_request_reset()
            elif choice == "4":
                self.handle_reset_password()
            elif choice == "5":
                self.handle_change_password()
            elif choice == "6":
                self.handle_view_profile()
            elif choice == "7":
                self.handle_logout()
            elif choice == "0":
                print("Thoat chuong trinh")
                break
            else:
                print("Lua chon khong hop le")
                
            print()
            
    def show_menu(self):
        print("=== SOCIAL MINI - MENU CHINH ===")
        print("1. Đang ki")
        print("2. Đang nhap")
        print("3. Yeu cau quen mat khau")
        print("4. Reset mật khau")
        print("5. Doi mat khau")
        print("6. Xem thong tin ca nhan")
        print("7. Đang xuat")
        print("0. Thoat")
        print("=================================")   
        
    def input_non_empty(self, promt):
        while True:
            v = input(promt).strip()
            if v == "0":
                return None
            if v:
                return v 
            print("Khong duoc de trong. Nhap lai hoac 0 de quay lai.") 
            
    def pause(self):
        input("Nhan Enter de tiep tuc...")
        
    def handle_register(self):
        print("___DANG KI___")         
        username = self.input_non_empty("Username: ")
        if username is None: return 
        email = self.input_non_empty("Email: ")
        if email is None: return 
        password = self.input_non_empty("Password: ")
        if password is None: return
        
        try:
            user = self.auth.register(username = username,email = email, password = password)
            print("Dang ki thanh cong")
        except Exception as e:
            print("Loi ",e)
        finally:
            self.pause()
            
    def handle_request_reset(self):
        print("--- YEU CAU RESET MAT KHAU ---")
        email = self.input_non_empty("Nhap email: ")
        if email is None: return
        try:
            code = self.auth.request_reset_password(email)
            print("Mã reset đã được gửi (mô phỏng):", code)
            print("Bạn có thể dùng mã này để reset mật khẩu.")
        except Exception as e:
            print("Lỗi:", e)
        finally:
            self.pause()

    def handle_reset_password(self):
        print("--- RESET MAT KHAU ---")
        email = self.input_non_empty("Nhap email: ")
        if email is None: return
        code = self.input_non_empty("Nhập ma reset: ")
        if code is None: return
        new_pw = self.input_non_empty("Nhập mat khau moi: ")
        if new_pw is None: return

        try:
            self.auth.reset_password(email=email, code=code, new_password=new_pw)
            print("Reset mat khau thanh cong.")
        except Exception as e:
            print("Loi:", e)
        finally:
            self.pause()

    def handle_login(self):
        print("--- ĐANG NHAP ---")
        identifier = self.input_non_empty("Username hoặc email: ")
        if identifier is None: return
        password = self.input_non_empty("Passwor: ")
        if password is None: return

        try:
            user = self.auth.login(identifier, password)
            self.current_user_id = user.id
            print(f"Đăng nhập thành công. Xin chào {user.username}!")
        except Exception as e:
            print("Đăng nhập thất bại:", e)
        finally:
            self.pause()

    def handle_change_password(self):
        print("--- ĐỔI MẬT KHẨU ---")
        if not self.current_user_id:
            print("Bạn chưa đăng nhập. Vui lòng đăng nhập trước.")
            self.pause()
            return

        old_pw = self.input_non_empty("Nhập mật khẩu cũ (0 để quay lại): ")
        if old_pw is None: return
        new_pw = self.input_non_empty("Nhập mật khẩu mới (0 để quay lại): ")
        if new_pw is None: return

        try:
            self.auth.change_password(self.current_user_id, old_pw, new_pw)
            print("Đổi mật khẩu thành công.")
        except Exception as e:
            print("Lỗi:", e)
        finally:
            self.pause()

    def handle_view_profile(self):
        print("--- THÔNG TIN CÁ NHÂN ---")
        if not self.current_user_id:
            print("Bạn chưa đăng nhập.")
            self.pause()
            return
        user = self.user_manager.get_by_id(self.current_user_id)
        if not user:
            print("Không tìm thấy người dùng (có thể đã bị xóa).")
        else:
            print("ID:", user.id)
            print("Username:", user.username)
            print("Email:", user.email)
            print("Profile:", getattr(user, "profile", {}))
        self.pause()

    def handle_logout(self):
        if not self.current_user_id:
            print("Bạn chưa đăng nhập.")
        else:
            self.current_user_id = None
            print("Đã đăng xuất.")
        self.pause()

if __name__ == "__main__":
    app = App()
    app.run()