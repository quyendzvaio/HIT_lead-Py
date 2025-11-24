import json
import os
from models.user import User

class JsonStorage:
    def __init__(self, filepath="data/users.json"):
        self.filepath = filepath
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                json.dump([],f)
                
    def load_users(self):
        with open(self.filepath, "r") as f:
            raw = json.load(f)
        return [User.from_dict(u) for u in raw]
    
    def save_users(self, users):
        data = [u.to_dict() for u in users]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
