from models import Usuario
from sqlalchemy import (
    Column, Integer, String, ARRAY
)

class Psicologa(Usuario):

    __tablename__ = "psicologas"

    crp = Column(String(20), unique=True, nullable=False)
    especializacoes = Column(ARRAY[String], nullable=False)
    abordagem = Column(String(150), nullable=False)
    valor_consulta = Column(Integer, nullable=False)
