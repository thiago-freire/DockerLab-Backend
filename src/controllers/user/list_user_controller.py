from typing import Type
from src.services.user import ListUserService
from flask import Response
from src.errors import BadRequest

class ListUserController:
    
    def __init__(self, list_user_service: ListUserService) -> None:
        self.list_user_service = list_user_service

    def handler(self) -> Response:
        
        try:
            
            list_user = self.list_user_service.execute()
            
            return Response(status=201, response={"lista": list_user})
        except Exception as e:
            return Response(status=500, response={"error": e})