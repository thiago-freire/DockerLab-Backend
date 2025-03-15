from typing import Type
from models.entities.machine import Machine
from src.models.repositories.interfaces import MachineRepositoryInterface
from src.errors import AlReadyExists, BadRequest

class CreateMachineService:
  def __init__(self, machine_repository: MachineRepositoryInterface) -> None:
    self.machine_repository = machine_repository

  def execute(self, name: Type[str], ip: Type[str], user: Type[str], password: Type[str], port: Type[int]) -> Machine:
    
    verify_data = isinstance(name, str) and isinstance(ip, str) and isinstance(password, str) and isinstance(user, str) and isinstance(port, int)

    if not verify_data:
      raise BadRequest("dados informados estão incorretos")
    
    ip_exists = self.machine_repository.get_machine_by_ip(ip)

    if ip_exists:
      raise AlReadyExists("Já existe uma máquina utilizando este IP")

    machine = self.machine_repository.create_machine(ip=ip, name=name, password=password, port=port, user=user)

    return machine