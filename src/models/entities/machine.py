from sqlalchemy import Column, String, Integer, UniqueConstraint, DateTime
from sqlalchemy.sql import func
from src.infra.configs import Base

from datetime import timedelta
from sqlalchemy.orm import relationship

class Machine(Base):
    
    __tablename__ = "maquina"

    id = Column("id_maquina", Integer, primary_key=True, autoincrement=True)
    name = Column("nome", String(15), nullable=True)
    ip = Column("ip", String(15), nullable=False)
    user = Column("usuario", String(30), nullable=False)
    password = Column("senha", String(200), nullable=False)
    port = Column("porta", String(1), nullable=False)
    create_date = Column("data_cadastro", DateTime(timezone=True), default=func.now(), nullable=False)

    __table_args__ = (UniqueConstraint('ip', name='_ip_machine'),)

    def __init__(self, ip, name, user, password, port) -> None:
        self.ip = ip 
        self.name = name
        self.user = user
        self.password = password
        self.port = port

    def __repr__(self) -> str:
        return f"Machine [name = {self.name}]"

    def __eq__(self, other) -> bool:
        return self.ip == other.ip

    def to_dict(self):
        return {
            "id": self.id,
            "Network": self.ip,
            "Nome": self.name,
            "login": self.user,
            "porta": self.port,
            "senha": self.password,
            "create_date": self.create_date.strftime('%d/%m/%Y')
        }
