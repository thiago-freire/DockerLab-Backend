import requests
import json

from src.models.repositories.interfaces import MachineRepositoryInterface

class MachineInfoService:

  def __init__(self, machine_repository: MachineRepositoryInterface) -> None:
    self.machine_repository = machine_repository
    
  def execute(self):
    
    machines = self.machine_repository.get_all()

    lista = []
    for machine in machines:
      print(machine)
      x = requests.get(f'http://{machine["ip"]}:5001/')
      lista.append()

    print(lista)

    return json.loads(json.dumps(lista))