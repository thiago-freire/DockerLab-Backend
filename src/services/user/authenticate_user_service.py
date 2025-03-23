import datetime
from werkzeug.security import check_password_hash
from src.configs import configs_env
from src.models.repositories.interfaces import UserRepositoryInterface
from src.errors import BadRequest

class AutheticateUserService:
    
    def __init__(self, user_repository: UserRepositoryInterface) -> str:
        self.user_repository = user_repository
        
    def execute(self, login: str, password: str):
            
            user_exists = self.user_repository.get_user_by_login(login=login)

            print(user_exists.to_dict())

            if not user_exists:
                raise BadRequest("email ou password estão incorretos")
            
            # decoded_password = check_password_hash(user_exists.password, password)

            # if not decoded_password:
            #     raise BadRequest("email ou password estão incorretos")
            
    
            time = datetime.timedelta(hours=10)
            # payload = {
            #     "id": user_exists.id,
            #     "exp": datetime.datetime.now(datetime.timezone.utc) + time
            # }

            # token = jwt.encode(payload, configs_env["secret_key"], algorithm="HS256")

            return user_exists