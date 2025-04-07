# Carteira de Ações - Front-end

Este projeto faz parte da minha avaliação na Pós-Graduação em Engenharia de Software da PUC-Rio. Trata-se de uma API RESTful desenvolvida em Flask para gerenciamento de uma carteira de ações. Permite registrar ações, calcular valorização e consultar informações atualizadas.

Esta API pode ser gerenciada pelo frontend abaixo:
https://github.com/cclguedes/Carteira_Acoes_API_Frontend

## Funcionalidades

- Listagem de ações cadastradas
- Adição de novas ações
- Remoção de ações
- Cálculo automático:
  - Valor atual da ação (via lógica backend)
  - Valor total investido
  - Valorização percentual desde a compra

## Tecnologias utilizadas

- [Flask](https://flask.palletsprojects.com/)
- [Flask-OpenAPI3](https://pypi.org/project/flask-openapi3/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLite](https://www.sqlite.org/)

## Instalação

# Clone o repositório
git clone https://github.com/cclguedes/Carteira_Acoes_API_Backend

# Entre na pasta do projeto
cd carteira_acoes_api_backend

# Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
python app.py