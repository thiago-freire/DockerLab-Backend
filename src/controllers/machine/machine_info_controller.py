from typing import Type
from flask import Request, Response
from src.services.machine import MachineInfoService

class MachineInfoController:
    def __init__(self, machine_info_service: MachineInfoService) -> None:
        self.machine_info_service = machine_info_service

    def handler(self, request: Type[Request]) -> Response:

        try:

            ip = request.get_json().get('ip')
            machineInfo = self.machine_info_service.execute(ip)

            return Response(status=201, response={"machine": machineInfo})
        
        except Exception as e:
            print(e)
            return Response(status=500, response={"error": str(e)})