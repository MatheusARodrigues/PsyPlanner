from pydantic import BaseModel
from typing import List

class PsicologaBase(BaseModel):
    # Informações específicas que queremos requisitar
    id: int
    crp: str
    especializacoes: List[str]
    abordagem: str
    valor_consulta: int

    class Config:
        from_attributes = True

class PsicologaInformacoes(PsicologaBase):
    id: int
    crp: str
    especializacoes: List[str]
    abordagem: str
    valor_consulta: int
    usuario_id: int