from typing import Type
from src.services.user import AutheticateUserService
from src.errors import BadRequest
from flask import Request, Response

class AuthenticateUserController:
    def __init__(self,  authenticate_user_service: Type[AutheticateUserService]) -> Response:
        self.authenticate_user_service = authenticate_user_service
        
    def handler(self, request: Type[Request]) -> Response:
        password = request.get_json().get('password')
        email = request.get_json().get('login')

        data_exists = all([password, email])

        try:
            if not data_exists:
                raise BadRequest("Precisar enviar todos os dados: email e senha")
            
            user_exists = self.authenticate_user_service.execute(email, password)

            return Response(status=200, response={"user": {
                                                        "id": user_exists.id,
                                                        "name": user_exists.name,
                                                        "email": user_exists.email,
                                                        "login": user_exists.login,
                                                        "profile": user_exists.profile
                                                    }})
        except BadRequest as bad:
            return Response(status=bad.status_code, response={"error": bad.message})