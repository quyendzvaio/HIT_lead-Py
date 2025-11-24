from typing import Optional
from models.user import User
from untils.security import SecurityHelper
import datetime

class UserManager:
    def __init__(self,storage_adapter = None):
        self.storage_adapter = storage_adapter
        self.users: dict[str,User] = {}
        
    def create_user(self,username, email, password_hash, security):
        user = User(
            id = security.generate_user_id(),
            username = username,
            email = email,
            password_hash = password_hash,
            created_at= datetime.datetime.utcnow().isoformat(),
            profile= {}
        )
        
        self.add_user(user)
        return user
    
    def add_user(self,user: User):
        if self.get_by_email(user.email) is not None:
            raise ValueError("Email da ton tai")
        
        if self.get_by_username(user.username) is not None:
            raise ValueError("Username da ton tai")
        
        self.users[user.id] = user
        
    def get_by_email(self,email: str) -> Optional[User]:
        return next((ema for ema in self.users.values() if ema.email == email), None)
        # for ema in self.users.values():
        #     if ema.email == email:
        #         return ema
        # return None
        
    def get_by_id(self,user_id: str) -> Optional[User]:
        return self.users.get(user_id)
    
    def get_by_username(self,username: str) -> Optional[User]:
        return next((name for name in self.users.values() if name.email == username), None)
    
    def update_user(self,user: User):
        if user.id not in self.users:
            raise ValueError("User khong ton tai")
        
        self.users[user.id] = user
        
    def delete_user(self,user_id: str):
        if user_id in self.users:
            del self.users[user_id]
            
    def list_all_users(self):
        return list(self.users.values())