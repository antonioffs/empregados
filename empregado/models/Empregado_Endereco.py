from sqlalchemy import Column, Integer, String, DateTime
from empregado.database import Base
from sqlalchemy.sql import func

class Empregado_endereco(Base):
    __tablename__ = 'empregado_endereco'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    id_empregado = Column('id_empregado', Integer, nullable=False)
    logradouro = Column('logradouro', String(100), nullable=False)
    bairro = Column('bairro', String(70), nullable=False)
    cidade = Column('cidade', String(70), nullable=False)
    estado = Column('estado', String(50), nullable=False)
    numero = Column('numero', Integer, nullable=False)
    cep = Column('cep', Integer, nullable=False)

    def __init__(self, _id=None, id_empregado=None, logradouro=None, bairro=None, cidade=None, estado=None, numero=None, cep=None):
        self.id_empregado = id_empregado
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.cep = cep

    def to_json(self):
        return {"id": self.id,
                "id_empregado": self.id_empregado,
                "logradouro": self.logradouro,
                "bairro": self.bairro,
                "cidade": self.cidade,
                "estado": self.estado,
                "numero": self.numero,
                "cep": self.cep}
