from typing import Dict
from app.enums.roles import Role
from app.enums.user_type import UserType
from app.repositories.security_repository import SecurityRepository


class SecurityService:
    def __init__(self):
        self.security_repository = SecurityRepository()
    def login(self, data):
        if 'email' not in data:
            return False
        if 'password' not in data:
            return False
        user = self.security_repository.login(data)
        if user is not None:
            return True
        return False
    def register(self, data) -> bool:
        if 'email' not in data:
            return False
        if 'password' not in data:
            return False
        data_to_register = {
            'email': data['email'],
            'password': data['password'],
            'user_type': data['user_type'],
            'roles': self.__get_role_for_user(data['user_type'])
        }
        self.security_repository.register(data=data_to_register)
        return True
    def __get_role_for_user(self, user_type: str) -> list[str]:
        if user_type == UserType.BODEGUERO.value:
            return [Role.INVENTARIOS.value]
        if user_type == UserType.SECRETARIA.value:
            return [Role.INVENTARIOS.value, Role.MENSAJERIA.value]
        if user_type == UserType.ADMIN.value:
            return [Role.ADMINISTRADOR.value]
        return Role.OTHER.value
    