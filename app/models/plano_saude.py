from sqlalchemy import Column, Integer, String, Table, ForeignKey

class PlanoSaude():
    __tablename__ = "planos_saude"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True)
    registro_ans = Column(String, unique=True)

psicologa_plano = Table(
    "psicologa_plano",

    Column("psicologa_id", Integer, ForeignKey("psicologas.id")),
    Column("plano_id", Integer, ForeignKey("planos_saude.id"))
)
