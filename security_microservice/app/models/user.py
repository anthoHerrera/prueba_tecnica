from dataclasses import dataclass

class User:
    password: str
    email: str
    role: str
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data) 
    @classmethod
    def to_dict(cls, data):
        return {
            'password': data.password,
            'email': data.email,
            'role': data.role
        }
        