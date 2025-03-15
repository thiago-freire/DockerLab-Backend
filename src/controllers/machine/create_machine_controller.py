from typing import Type
from flask import Response, Request
from src.errors import BadRequest
from src.services.machine import CreateMachineService

class CreateMachineController:
    
    def __init__(self, create_machine_service: CreateMachineService) -> None:
        self.create_machine_service = create_machine_service

    def handler(self, request: Type[Request]) -> Response:

        name = request.get_json().get('name')
        ip = request.get_json().get('ip')
        password = request.get_json().get('password')
        port = request.get_json().get('port')
        user = request.get_json().get('user')

        print(name, type(name))
        print(ip, type(ip))
        print(password, type(password))
        print(port, type(port))
        print(user, type(user))
        

        data_exists = all([name, ip, password, port, user])

        try:

            if not data_exists:
                raise BadRequest("Precisa enviar todos os dados: name, ip, password, port e user")

            machine = self.create_machine_service.execute(name=name, ip=ip, password=password, port=port, user=user)

            return Response(status=201, response={"machine": machine})
        
        except Exception as e:
            print(e)
            return Response(status=500, response={"error": str(e)})