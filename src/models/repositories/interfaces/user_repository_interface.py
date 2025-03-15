from abc import ABC, abstractmethod

from models.entities.user import User

class UserRepositoryInterface(ABC):
    """ classe abstrata que serve """
    @abstractmethod
    def create_user(self, name, email , profile) -> User:
        """ metodo para criar usuário """
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_user_by_email(self, email: str):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_user_by_id(self, id: int):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def delete_user(self, user: User):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def update_user(self, user: User):
        raise NotImplementedError("Necessario implementar o método")