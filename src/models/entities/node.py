from sqlalchemy import Column, String, Integer, UniqueConstraint, ForeignKey
from src.infra.configs import Base
from sqlalchemy.orm import relationship

class Node(Base):
    
    __tablename__ = "nodocker"

    id = Column("id_nodocker", Integer, primary_key=True, autoincrement=True)
    name = Column("nome", String(100), nullable=False)
    id_machine = Column("id_maquina", Integer, ForeignKey('maquina.id_maquina'))
    id_user = Column("id_usuario", Integer, ForeignKey('usuario.id_usuario'))
    cpu_cores = Column("cpu_cores", Integer, nullable=False)
    ram = Column("ram", Integer, nullable=False)
    device = Column("device", String(1), nullable=False)
    network = Column("network", String(1), nullable=False)

    # __table_args__ = (UniqueConstraint('email', name='_email_uc'),)

    user = relationship("User")
    machine = relationship("Machine")

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
