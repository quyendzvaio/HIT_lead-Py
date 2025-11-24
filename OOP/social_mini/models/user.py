
import time
class User:
    def __init__(self,id:str ,username:str ,email:str ,password_hash:str ,created_at:str ,profile:dict):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at or time.time.utcnow().isoformat()
        self.profile = profile or {}
    
    @classmethod
    def from_dict(cls,data: dict)-> "User":
        return cls(
            id = data.get("id"),
            username = data.get("username"),
            email = data.get("email"),
            password_hash = data.get('password_hash'),
            profile = data.get('profile',{})
            )
    def to_dict(self)-> dict:
        return {
            "id":self.id,
            "username":self.username,
            "email":self.email,
            "password_hash":self.password_hash,
            "creat_at":self.created_at,
            "profile":self.profile
        }
    def set_password(self,plain_password: str,*,security_helper):
        self.password_hash = security_helper.hash_password(plain_password)
    def verify_password(self,plain_password:str,*,security_helper)->bool:
        return security_helper.verify_password(plain_password,self.password_hash)
    def update_profile(self,**kwargs):
        for key ,value in kwargs.item():
            self.profile[key] = value