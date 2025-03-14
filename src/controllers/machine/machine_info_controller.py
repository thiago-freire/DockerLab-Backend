from flask import Response
from src.services.machine import MachineInfoService

class MachineInfoController:
    def __init__(self, machine_info_service: MachineInfoService) -> None:
        self.machine_info_service = machine_info_service

    def handler(self) -> Response:

        try:

            machineInfo = self.machine_info_service.execute()

            return Response(status=201, response={"info": machineInfo})
        
        except Exception as e:
            print(e)
            return Response(status=500, response={"error": str(e)})