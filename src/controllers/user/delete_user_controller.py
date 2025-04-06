from typing import Type
from src.services.user import DeleteUserService
from flask import Response, Request
from src.errors import BadRequest

class DeleteUserController:
    
    def __init__(self, delete_user_service: DeleteUserService) -> None:
        self.delete_user_service = delete_user_service

    def handler(self, request: Type[Request]) -> Response:
        
        id = request.get_json().get('id')
        name = request.get_json().get('name')
        email = request.get_json().get('email')
        profile = request.get_json().get('profile')
        login = request.get_json().get('login')
        password = request.get_json().get('password')

        data_exists = all([id, name, email, profile, login, password])

        try:
            if not data_exists:
                raise BadRequest("Precisa enviar todos os dados: name, profile, password, login e email")
            

            resp = self.delete_user_service.execute(id= id,
                                                    name= name,
                                                    email =  email,
                                                    profile=profile,
                                                    login=login,
                                                    password=password)

            return Response(status=201, response={"resp": resp})
        except Exception as e:
            print(e)
            return Response(status=500, response={"error": str(e)})