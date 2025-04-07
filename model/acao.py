from sqlalchemy import Column, String, Integer, Float
from typing import Union

from model.base import Base

class Acao(Base):
    __tablename__ = 'acao'  # Tabela chamada 'acao'

    # Definição dos campos
    id = Column("pk_acao", Integer, primary_key=True)
    ticker = Column(String(10), unique=True)
    qtd = Column(Integer)
    valor = Column(Float)

    def __init__(self, ticker: str, qtd: int, valor: float):
        """
        Cria um objeto da classe Acao

        Arguments:
            ticker: código do ativo (ex: 'PETR4', 'VALE3')
            qtd: quantidade do ativo
            valor: valor do ativo
        """
        self.ticker = ticker
        self.qtd = qtd
        self.valor = valor

