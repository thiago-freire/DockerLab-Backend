import requests
import json

from models.repositories.interfaces.machine_repository_interface import MachineRepositoryInterface

class MachineInfoService:

  def __init__(self, machine_repository: MachineRepositoryInterface) -> None:
    self.machine_repository = machine_repository
    
  def execute(self):
    
    machines = self.machine_repository.get_all()

    lista = []
    for machine in machines:
      x = requests.get(f'http://{machine.ip}:5001/')
      lista.append(x.text)

    return json.loads(lista)