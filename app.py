from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
import requests

from sqlalchemy.exc import IntegrityError

from model import Session, Acao
from schemas import *
from flask_cors import CORS

info = Info(title="Carteira de Ações API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Documentação da API")
acao_tag = Tag(name="Ação", description="Adição, visualização e remoção de ações na base")


def obter_valor_atual(ticker: str) -> float:
    try:
        url = f"https://ledev.com.br/api/cotacoes/{ticker.upper()}"
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        return float(dados['price'])  # <- corrigido aqui
    except Exception:
        return 0.0



def apresenta_acao(acao: Acao):
    valor_atual = obter_valor_atual(acao.ticker)
    valor_total = round(valor_atual * acao.qtd, 2)
    
    if acao.valor != 0:
        valorizacao = round(((valor_atual - acao.valor) / acao.valor) * 100, 2)
    else:
        valorizacao = 0.0

    return {
        "ticker": acao.ticker,
        "qtd": acao.qtd,
        "valor": acao.valor,
        "valor_atual": valor_atual,
        "valor_total": valor_total,
        "valorizacao": valorizacao
    }



def apresenta_acoes(acoes: list[Acao]):
    return {
        "acoes": [apresenta_acao(acao) for acao in acoes]
    }


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para a documentação da API."""
    return redirect('/openapi')


@app.post('/acao', tags=[acao_tag],
          responses={"200": AcaoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_acao(form: AcaoSchema):
    """Adiciona uma nova ação à base de dados"""
    acao = Acao(
        ticker=form.ticker,
        qtd=form.qtd,
        valor=form.valor
    )
    try:
        session = Session()
        session.add(acao)
        session.commit()
        return apresenta_acao(acao), 200

    except IntegrityError:
        return {"mesage": "Ação com esse ticker já existe na base"}, 409

    except Exception:
        return {"mesage": "Erro ao adicionar ação"}, 400


@app.get('/acoes', tags=[acao_tag],
         responses={"200": ListagemAcoesSchema, "404": ErrorSchema})
def get_acoes():
    """Busca todas as ações cadastradas na base"""
    session = Session()
    acoes = session.query(Acao).all()

    if not acoes:
        return {"acoes": []}, 200
    else:
        return apresenta_acoes(acoes), 200


@app.get('/acao', tags=[acao_tag],
         responses={"200": AcaoViewSchema, "404": ErrorSchema})
def get_acao(query: AcaoBuscaSchema):
    """Busca uma ação pelo ticker"""
    session = Session()
    acao = session.query(Acao).filter(Acao.ticker == query.ticker).first()

    if not acao:
        return {"mesage": "Ação não encontrada"}, 404
    else:
        return apresenta_acao(acao), 200


@app.delete('/acao', tags=[acao_tag],
            responses={"200": AcaoDelSchema, "404": ErrorSchema})
def del_acao(query: AcaoBuscaSchema):
    """Remove uma ação da base pelo ticker"""
    ticker = unquote(unquote(query.ticker))
    session = Session()
    count = session.query(Acao).filter(Acao.ticker == ticker).delete()
    session.commit()

    if count:
        return {"mesage": "Ação removida", "nome": ticker}, 200
    else:
        return {"mesage": "Ação não encontrada"}, 404