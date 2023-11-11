from typing import Dict
from app.persistence.mongo_client import get_collection


class SecurityRepository:
    def __init__(self) -> None:
        self.users = get_collection("users")
    def login(self, data: Dict):
        return self.users.find_one({"password": data['password']})
    def register(self, data: Dict):
        return self.users.insert_one(data)
    