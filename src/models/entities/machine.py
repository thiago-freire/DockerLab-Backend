from sqlalchemy import Column, String, Integer, UniqueConstraint, DateTime
from sqlalchemy.sql import func
from src.infra.configs import Base

from datetime import timedelta
# from sqlalchemy.orm import relationship

class Machine(Base):
    __tablename__ = "machine"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("nome", String(15), nullable=True)
    ip = Column("ip", String(15), nullable=False)
    user = Column("usuario", String(30), nullable=False)
    password = Column("senha", String(200), nullable=False)
    port = Column("porta", String(1), nullable=False)
    # create = Column("cadastro", DateTime(timezone=True), default=func.now() - timedelta(hours=3), nullable=False)

    __table_args__ = (UniqueConstraint('ip', name='_ip_machine'),)

    # scenarios = relationship("Scenario", back_populates='user', uselist=True)
    # gambiarras = relationship("Gambiarra", back_populates='udb_baseser', uselist=True)
    # regions = relationship("Region", back_populates='user', uselist=True)
    # files = relationship("File", back_populates="user", uselist=True)

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
            "ip": self.ip,
            "name": self.name,
            "user": self.user,
            "port": self.port,
            "password": self.password
        }
