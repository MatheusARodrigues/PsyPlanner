from pydantic import BaseModel
from datetime import datetime

class UsuarioBase(BaseModel): 
    id: int
    email: str
    senha_hash: str

    class Config:
        from_attributes = True

class UsuarioInformacoes(UsuarioBase):
    id: int
    nome: str
    email: str
    senha_hash: str
    telefone: str
    ativo: bool = True
    data_criacao = datetime
    type: str = "usuario"