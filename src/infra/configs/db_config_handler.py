import os
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.configs import configs_env

load_dotenv()

class DbConfigHandler:
    def __init__(self) -> None:
        self.__connection_url = configs_env["url_database"]        
        self.session: Optional[Session] = None

    def getEngine(self):
        engine = create_engine(self.__connection_url)

        return engine
    
    def __enter__(self):
        engine = create_engine(self.__connection_url)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()