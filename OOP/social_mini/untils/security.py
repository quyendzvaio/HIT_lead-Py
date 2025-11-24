import bcrypt
import uuid
import random

class SecurityHelper:
    
    def hash_password(self,password: str)->str:
        password_bytes = password.encode("utf-8")
        hashed = bcrypt.hashpw(password_bytes,bcrypt.gensalt())
        return hashed.decode("utf-8")
    
    def verify_password(self,password: str,hashed:str)->bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed.encode("utf-8")
        )    
    def generate_reset_code(self)->str:
        """
        tao ma xac thuc ngau nhien de reset mat khau
        """
        return f"{random.randint(0,999999):06d}"
    
    def generate_user_id(self)->str:
        return str(uuid.uuid4())