from src.services.machine import ListMachineService
from flask import Response

class ListMachineController:
    
    def __init__(self, list_machine_service: ListMachineService) -> None:
        self.list_machine_service = list_machine_service

    def handler(self) -> Response:
        
        try:
            
            list_machine = self.list_machine_service.execute()
            
            return Response(status=201, response={"lista": list_machine})
        except Exception as e:
            return Response(status=500, response={"error": e})