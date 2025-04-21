from sqlalchemy import (Column, Integer, String, Boolean, func, DateTime)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__="usuario"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email=Column(String(150), unique= True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    telefone = Column(String(20))
    ativo = Column(Boolean, default=True, autoincrement=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

    # type = Column(String(20))

    # __mapper_args__= {
    #     'polymorphic_on' : type,
    #     'polymorphic_identity' : 'usuario'
    # }
    

