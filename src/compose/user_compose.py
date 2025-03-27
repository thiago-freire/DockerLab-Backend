from src.models.repositories.user_repository import UserRepository


from src.controllers.user import (
    CreateUserController,
    ListUserController,
    AuthenticateUserController,
    UpdateUserController
)

from src.services.user import (
    CreateUserService,
    ListUserService,
    AutheticateUserService,
    UpdateUserService
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

def authenticate_user_compose():
    
    user_repository = UserRepository()
    authenticate_user_service = AutheticateUserService(user_repository)
    authenticate_user_controller = AuthenticateUserController(authenticate_user_service)

    return authenticate_user_controller

def update_user_compose():

    user_repository = UserRepository()
    update_user_service = UpdateUserService(user_repository)
    update_user_controller = UpdateUserController(update_user_service)

    return update_user_controller