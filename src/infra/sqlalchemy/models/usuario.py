from sqlalchemy import Column, Integer, String, TIMESTAMP, VARCHAR
from src.infra.sqlalchemy.config.database import Base

from datetime import datetime 

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nome = Column(VARCHAR(255), nullable=False)
    senha = Column(VARCHAR(120), nullable=False)
    email = Column(VARCHAR(180), unique=True, nullable=False)
    telefone = Column(String(11), nullable=False)
    funcao = Column(Integer, nullable=False, default=3)
    foto = Column(VARCHAR(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=True, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return "<Usuario(nome='%s')>" % (self.nome)

