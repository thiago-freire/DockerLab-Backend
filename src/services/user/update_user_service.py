from typing import Type
from src.models.entities.user import User
from werkzeug.security import generate_password_hash
from src.models.repositories.interfaces import UserRepositoryInterface
from src.errors import BadRequest

class UpdateUserService:
  
  def __init__(self, user_repository: UserRepositoryInterface) -> User:
    self.user_repository = user_repository

  def execute(self, id: Type[int], name: Type[str], email: Type[str], profile: Type[str], login: Type[str], password: Type[str]) -> bool:
    
    verify_data = isinstance(id, int) and isinstance(name, str) and isinstance(profile, str) and \
                  isinstance(email, str) and isinstance(login, str) and isinstance(password, str)

    if not verify_data:
      raise BadRequest("dados informados estão incorretos")
    
    password_hash = generate_password_hash(password)

    user = User(name=name, login=login, profile=profile, password=password_hash, email=email)
    user.id = id

    result = self.user_repository.update_user(user=user)

    return result