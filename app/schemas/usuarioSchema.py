from pydantic import BaseModel, Field
from datetime import datetime

class UsuarioBase(BaseModel): 
    email: str
    senha_hash: str


class UsuarioInformacoes(UsuarioBase):
    nome: str
    email: str
    senha_hash: str
    telefone: str
    ativo: bool = True
    data_criacao: datetime = Field(default_factory=datetime.now) 
    # type: str = "usuario"

    class Config:
        from_attributes = True