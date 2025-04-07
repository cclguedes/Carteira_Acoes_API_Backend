from pydantic import BaseModel
from typing import List
from model.acao import Acao
import requests

class AcaoSchema(BaseModel):
    """ Define como uma nova ação a ser inserida deve ser representada """
    ticker: str = "VALE3"
    qtd: int = 10
    valor: float = 58.50


class AcaoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura para busca por ticker """
    ticker: str = "VALE3"


class ListagemAcoesSchema(BaseModel):
    """ Define como uma listagem de ações será retornada """
    acoes: List[AcaoSchema]


def busca_valor_atual(ticker: str) -> float:
    try:
        response = requests.get(f"https://ledev.com.br/api/cotacoes/{ticker}")
        if response.status_code == 200:
            data = response.json()
            valor = data.get("price")
            if valor:
                return float(valor)
    except Exception as e:
        print(f"[ERRO] Falha ao buscar valor atual de {ticker}: {e}")
    return 0.0


def apresenta_acoes(acoes: List[Acao]):
    result = []
    for acao in acoes:
        valor_atual = busca_valor_atual(acao.ticker)
        valor_total = valor_atual * acao.qtd
        if acao.valor != 0:
            valorizacao = round(((valor_atual - acao.valor) / acao.valor) * 100, 2)
        else:
            valorizacao = 0.0
        result.append({
            "ticker": acao.ticker,
            "qtd": acao.qtd,
            "valor": acao.valor,
            "valor_atual": valor_atual,
            "valor_total": valor_total,
            "valorizacao": valorizacao
        })
    return {"acoes": result}


def apresenta_acao(acao: Acao):
    valor_atual = busca_valor_atual(acao.ticker)
    valor_total = valor_atual * acao.qtd
    if acao.valor != 0:
        valorizacao = round(((valor_atual - acao.valor) / acao.valor) * 100, 2)
    else:
        valorizacao = 0.0

    return {
        "id": acao.id,
        "ticker": acao.ticker,
        "qtd": acao.qtd,
        "valor": acao.valor,
        "valor_atual": valor_atual,
        "valor_total": valor_total,
        "valorizacao": valorizacao
    }


class AcaoViewSchema(BaseModel):
    """ Define como uma ação será retornada individualmente """
    id: int = 1
    ticker: str = "VALE3"
    qtd: int = 10
    valor: float = 58.50
    valor_atual: float = 52.68
    valor_total: float = 526.80
    valorizacao: float = -9.96


class AcaoDelSchema(BaseModel):
    """ Define como será o retorno da remoção de uma ação """
    mesage: str
    ticker: str
