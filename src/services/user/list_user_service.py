from typing import Type
from src.models.repositories.interfaces import UserRepositoryInterface

class ListUserService:
  
  def __init__(self, user_repository: UserRepositoryInterface):
    self.user_repository = user_repository

  def execute(self):

    list_users = self.user_repository.get_all()

    return list_users