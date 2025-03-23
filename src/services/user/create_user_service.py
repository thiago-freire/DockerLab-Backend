from typing import Type
from src.models.entities.user import User
from werkzeug.security import generate_password_hash
from src.models.repositories.interfaces import UserRepositoryInterface
from src.errors import AlReadyExists, BadRequest

class CreateUserService:
  
  def __init__(self, user_repository: UserRepositoryInterface) -> User:
    self.user_repository = user_repository

  def execute(self, name: Type[str], email: Type[str], profile: Type[str], login: Type[str], password: Type[str]):
    
    verify_data = isinstance(name, str) and isinstance(profile, str) and isinstance(email, str) and isinstance(login, str) and isinstance(password, str)

    if not verify_data:
      raise BadRequest("dados informados estão incorretos")
    
    email_exists = self.user_repository.get_user_by_email(email)

    if email_exists:
      raise AlReadyExists("Já existe um usuário utilizando este email")
    
    password_hash = generate_password_hash(password)

    user = self.user_repository.create_user(name=name, email=email, profile=profile, login=login, password=password_hash)

    return user