from src.models.repositories.user_repository import UserRepository


from src.controllers.user import (
    CreateUserController
)

from src.services.user import (
    CreateUserService
)

def create_user_compose():

    user_repository = UserRepository()
    create_user_service = CreateUserService(user_repository)
    create_user_controller = CreateUserController(create_user_service)

    return create_user_controller