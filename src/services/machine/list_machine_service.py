from typing import Type
from src.models.repositories.interfaces import MachineRepositoryInterface

class ListMachineService:
  
  def __init__(self, machine_repository: MachineRepositoryInterface):
    self.machine_repository = machine_repository

  def execute(self):

    list_machines = self.machine_repository.get_all()

    return list_machines