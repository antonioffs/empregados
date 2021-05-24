from sqlalchemy import Column, Integer, String, DateTime
from empregado.database import Base
from sqlalchemy.sql import func

class Empregado(Base):
    __tablename__ = 'empregado'

    id = Column('id', Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = Column('nome', String(150), nullable=False)
    sexo = Column('sexo', String(15), nullable=False)
    data_criacao = Column('data_criacao', DateTime(timezone=True), server_default=func.now(), nullable=False)
    idade = Column('idade', Integer, nullable=False)
    salario = Column('salario', Integer, nullable=False)

    def __init__(self, _id=None, nome=None, sexo=None, data_criacao=None, idade=None, salario=None):
        self.id = _id
        self.nome = nome
        self.sexo = sexo
        self.data_criacao = data_criacao
        self.idade = idade
        self.salario = salario

    def to_json(self):
        return {"id": self.id,
                "nome": self.nome,
                "sexo": self.sexo,
                "data_criacao": self.data_criacao,
                "idade": self.idade,
                "salario": self.salario
                }

    def __repr__(self):
        return

