from src.models.repositories.user_repository import UserRepository


from src.controllers.user import (
    CreateUserController,
    ListUserController
)

from src.services.user import (
    CreateUserService,
    ListUserService
)

def create_user_compose():

    user_repository = UserRepository()
    create_user_service = CreateUserService(user_repository)
    create_user_controller = CreateUserController(create_user_service)

    return create_user_controller

def list_user_compose():

    user_repository = UserRepository()
    list_user_service = ListUserService(user_repository)
    list_user_controller = ListUserController(list_user_service)

    return list_user_controller