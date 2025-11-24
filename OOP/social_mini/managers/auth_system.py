from typing import Optional
from models.user import User
from managers.user_manager import UserManager


class AuthSystem:
    def __init__(self, user_manager, security_helper):
        self.user_manager = user_manager
        self.security = security_helper
        self.reset_tokens = {}  # email → mã reset password

    def register(self, username, email, password) -> User:
        """
        - Kiểm tra username/email trùng
        - Hash mật khẩu
        - Tạo user mới
        - Lưu user vào UserManager
        """

        if self.user_manager.get_by_username(username):
            raise ValueError("Username đã tồn tại")

        if self.user_manager.get_by_email(email):
            raise ValueError("Email đã tồn tại")

        pw_hash = self.security.hash_password(password)

        user = self.user_manager.create_user(
            username= username,
            email= email,
            password_hash= pw_hash,
            security= self.security
            )

        return user

    def login(self, username_or_email, password) -> User:
        user = self.user_manager.get_by_username(username_or_email)

        if not user:
            user = self.user_manager.get_by_email(username_or_email)

        if not user:
            raise ValueError("User không tồn tại")

        if not self.security.verify_password(password, user.password_hash):
            raise ValueError("Sai mật khẩu")

        return user

    # ------------------------------------------------------------------
    def request_reset_password(self, email: str) -> str:
        """
        - Tìm user theo email
        - Generate code reset
        - Lưu vào reset_tokens
        - Trả mã reset
        """

        user = self.user_manager.get_by_email(email)
        if not user:
            raise ValueError("Email không tồn tại")

        code = self.security.generate_reset_code()

        # Lưu lại để kiểm tra
        self.reset_tokens[email] = code

        return code

    def reset_password(self, email: str, code: str, new_password: str):
        """
        - Kiểm tra mã reset đúng
        - Hash mật khẩu mới
        - Cập nhật user
        """

        # Check mã
        if email not in self.reset_tokens:
            raise ValueError("Không có yêu cầu reset mật khẩu")

        if self.reset_tokens[email] != code:
            raise ValueError("Sai mã reset")

        user = self.user_manager.get_by_email(email)

        new_pw_hash = self.security.hash_password(new_password)

        user.password_hash = new_pw_hash
        self.user_manager.update_user(user)
        
        del self.reset_tokens[email]

    def change_password(self, user_id: str, old_pw: str, new_pw: str):
        """
        - Tìm user theo ID
        - Verify mật khẩu cũ
        - Hash mật khẩu mới
        """

        user = self.user_manager.get_by_id(user_id)
        if not user:
            raise ValueError("User không tồn tại")

        # Verify mật khẩu cũ
        if not self.security.verify_password(old_pw, user.password_hash):
            raise ValueError("Mật khẩu cũ không đúng")

        new_pw_hash = self.security.hash_password(new_pw)

        user.password_hash = new_pw_hash

        self.user_manager.update_user(user)
