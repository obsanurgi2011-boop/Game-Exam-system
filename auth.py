import hashlib
import os
import json

class UserAuth:
    def __init__(self):
        self.users_file = 'users.json'
        self.current_user = None
        self.load_users()

    def load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, 'r', encoding='utf-8') as f:
                try:
                    self.users = json.load(f)
                except:
                    self.reset_admin()
        else:
            self.reset_admin()

    def reset_admin(self):
        self.users = [{'username': 'admin', 'password': hashlib.sha256('admin'.encode()).hexdigest(), 'role': 'admin'}]
        self.save_users()

    def save_users(self):
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, indent=4)

    def authenticate(self, username, password):
        hashed = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user['username'] == username and user['password'] == hashed:
                self.current_user = user
                return True
        return False

    def add_user(self, username, password, role):
        if any(u['username'] == username for u in self.users):
            return False
        hashed = hashlib.sha256(password.encode()).hexdigest()
        self.users.append({'username': username, 'password': hashed, 'role': role})
        self.save_users()
        return True
        
