import requests
import json

from src.models.repositories.interfaces import MachineRepositoryInterface

class MachineInfoService:

  def __init__(self, machine_repository: MachineRepositoryInterface) -> None:
    self.machine_repository = machine_repository
    
  def execute(self, ip: str):

    info = self.machine_repository.getMachineInfo(ip, requests.get, json.loads)    

    return info