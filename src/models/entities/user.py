from sqlalchemy import Column, String, Integer, UniqueConstraint, DateTime
from sqlalchemy.sql import func
from src.infra.configs import Base

from datetime import timedelta
from sqlalchemy.orm import relationship

class User(Base):
    
    __tablename__ = "usuario"

    id = Column("id_usuario", Integer, primary_key=True, autoincrement=True)
    name = Column("nome", String(100), nullable=False)
    email = Column(String(100), nullable=False)
    login = Column(String(90), nullable=False)
    profile = Column("perfil", String(1), nullable=False)
    password = Column("senha", String(100), nullable=False)
    create_date = Column("data_cadastro", DateTime(timezone=True), default=func.now(), nullable=False)

    __table_args__ = (UniqueConstraint('email', name='_email_uc'),)

    # nodes = relationship("Node", back_populates='user', uselist=True)

    def __init__(self, name, login, email, profile, password) -> None:
        self.name = name
        self.login = login
        self.email = email
        self.profile = profile
        self.password = password

    def __repr__(self) -> str:
        return f"User [name = {self.name}]"

    def __eq__(self, other) -> bool:
        return self.login == other.login

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "login": self.login,
            "email": self.email,
            "profile": self.profile,
            "password": self.password
        }
