from sqlalchemy import (
    Column, Integer, String, Boolean, func, DateTime
)

class Usuario():
    __tablename__="usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email=Column(String(150), unique= True, nullable=False, index=True)
    senha_hash = Column(String(255), nullable=False)
    telefone = Column(String(20))
    ativo = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

    type = Column(String(20))

    __mapper_args__= {
        'polymorphic_on' : type,
        'polymorphic_identity' : 'usuario'
    }
    

