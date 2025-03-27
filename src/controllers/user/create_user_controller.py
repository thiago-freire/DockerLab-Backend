from typing import Type
from src.services.user import CreateUserService
from flask import Response, Request
from src.errors import BadRequest

class CreateUserController:
    
    def __init__(self, create_user_service: CreateUserService) -> None:
        self.create_user_service = create_user_service

    def handler(self, request: Type[Request]) -> Response:
        
        name = request.get_json().get('name')
        email = request.get_json().get('email')
        profile = request.get_json().get('profile')
        login = request.get_json().get('login')
        password = request.get_json().get('password')

        data_exists = all([name, email, profile, login, password])

        try:
            if not data_exists:
                raise BadRequest("Precisa enviar todos os dados: name, profile, password, login e email")
            

            user = self.create_user_service.execute(name= name,
                                                    email =  email,
                                                    profile=profile,
                                                    login=login,
                                                    password=password)

            return Response(status=201, response={"user": user})
        except Exception as e:
            print(e)
            return Response(status=500, response={"error": str(e)})