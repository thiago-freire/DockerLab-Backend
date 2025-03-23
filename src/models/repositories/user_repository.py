from collections import namedtuple
from src.models.repositories.interfaces import UserRepositoryInterface 
from src.infra.configs.db_config_handler import DbConfigHandler
from src.models.entities.user import User

class UserRepository(UserRepositoryInterface):
    
    def create_user(self, name, email , profile, login, password):
        with DbConfigHandler() as connection:
            try:

                print(name, type(name))
                print(email, type(email))        
                print(profile, type(profile))
                print(login, type(login))
                print(password, type(password))
                
                new_user = User(name=name, email=email, profile=profile, login=login, password=password)
                connection.session.add(new_user)
                connection.session.commit()

                return new_user.to_dict()
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_user_by_email(self, email):
        with DbConfigHandler() as connection:
            try:
                user = connection.session.query(User).filter_by(email=email).first()

                return user
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_user_by_login(self, login):
        
        with DbConfigHandler() as connection:
            try:
                user = connection.session.query(User).filter_by(login=login).first()
                return user
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_user_by_id(self, id):
        with DbConfigHandler() as connection:
            try:
                user = connection.session.query(User).filter_by(id=id).first()

                return user
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def get_all(self):

        with DbConfigHandler() as connection:
            try:
                list_users = connection.session.query(User).all()

                return list_users
            except: 
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def delete_user(self, user: User) -> bool:
        with DbConfigHandler() as connection:
            try:
                connection.session.delete(user)
                connection.session.commit()

                return True
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    def update_user(self, user: User) -> bool:
        with DbConfigHandler() as connection:
            try:
                if not user:
                    return False
                
                u = connection.session.query(User).filter_by(id=id).first()

                u.name = user.name
                u.profile = user.profile
                
                return True
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()