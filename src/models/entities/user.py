from sqlalchemy import Column, String, Integer, UniqueConstraint
from src.infra.configs import Base
from sqlalchemy.orm import relationship

class User(Base):
    
    __tablename__ = "usuario"

    id = Column("id_usuario", Integer, primary_key=True, autoincrement=True)
    name = Column("nome", String(100), nullable=False)
    email = Column(String(100), nullable=False)
    profile = Column("perfil", String(1), nullable=False)

    __table_args__ = (UniqueConstraint('email', name='_email_uc'),)

    # nodes = relationship("Node", back_populates='user', uselist=True)

    def __init__(self, name, email, profile) -> None:
        self.name = name 
        self.email = email
        self.profile = profile

    def __repr__(self) -> str:
        return f"User [name = {self.name}]"

    def __eq__(self, other) -> bool:
        return self.email == other.email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "profile": self.profile
        }
