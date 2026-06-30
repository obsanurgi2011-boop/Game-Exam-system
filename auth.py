import json, os, hashlib

class UserAuth:
    def __init__(self):
        self.file = "data/users.json"
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):
            self.users = [{
                "username": "admin",
                "password": self.hash("admin"),
                "role": "admin"
            }]
            self.save()
        else:
            self.users = json.load(open(self.file))

        self.current_user = None

    def save(self):
        json.dump(self.users, open(self.file, "w"))

    def hash(self, p):
        return hashlib.sha256(p.encode()).hexdigest()

    def login(self, u, p):
        for x in self.users:
            if x["username"] == u and x["password"] == self.hash(p):
                self.current_user = x
                return True
        return False

    def add_user(self, u, p, role="student"):
        if any(x["username"] == u for x in self.users):
            return False
        self.users.append({
            "username": u,
            "password": self.hash(p),
            "role": role
        })
        self.save()
        return True
