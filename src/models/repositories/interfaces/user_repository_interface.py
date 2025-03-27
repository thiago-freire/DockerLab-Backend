from abc import ABC, abstractmethod

from src.models.entities.user import User

class UserRepositoryInterface(ABC):
    """ classe abstrata que serve """
    @abstractmethod
    def create_user(self, name, email , profile, login, password) -> User:
        """ metodo para criar usuário """
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_user_by_email(self, email: str):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_user_by_login(self, login: str) -> User:
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_user_by_id(self, id: int):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_all(self):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def delete_user(self, user: User)->bool:
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def update_user(self, user: User)->bool:
        raise NotImplementedError("Necessario implementar o método")