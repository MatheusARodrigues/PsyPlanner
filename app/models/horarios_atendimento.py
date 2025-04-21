from sqlalchemy import (
    Column, Integer, Boolean, Time, ForeignKey, CheckConstraint
)
from sqlalchemy.orm import relationship

class HorarioAtendimento(): 
    id = Column(Integer, primary_key=True)
    dia_semana = Column(Integer)
    hora_inicio = Column(Time)
    hora_fim = Column(Time)
    presencial = Column(Boolean)

    __table_args__ = (
        CheckConstraint('hora_fim > hora_inicio', name='chcceck_horario_valido' )
    )

    psicologa_id = Column(Integer, ForeignKey("psicologas.id"))
    psicologa = relationship("Psicologa", back_populates="horarios")
    