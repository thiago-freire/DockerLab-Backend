from abc import ABC, abstractmethod

from src.models.entities.machine import Machine

class MachineRepositoryInterface(ABC):
    
    """ classe abstrata que serve """
    @abstractmethod
    def create_machine(self, ip, name, user , password, port) -> Machine:
        """ metodo para criar usuário """
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_all(self):
        raise NotImplementedError("Necessario implementar o método")

    @abstractmethod
    def get_machine_by_name(self, name: str):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_machine_by_id(self, id: int):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def get_machine_by_ip(self, ip: str):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def delete_machine(self, machine: Machine):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def update_machine(self, machine: Machine):
        raise NotImplementedError("Necessario implementar o método")
    
    @abstractmethod
    def getMachineInfo(self, machine: Machine):
        raise NotImplementedError("Necessario implementar o método")