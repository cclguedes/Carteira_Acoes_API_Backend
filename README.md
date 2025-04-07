# Carteira de Ações - Front-end

Este projeto faz parte da minha avaliação na Pós-Graduação em Engenharia de Software da PUC-Rio. Trata-se de uma API RESTful desenvolvida em Flask para gerenciamento de uma carteira de ações. Permite registrar ações, calcular valorização e consultar informações atualizadas.

Esta API pode ser gerenciada pelo front-end abaixo:
https://github.com/cclguedes/Carteira_Acoes_API_Frontend

## Funcionalidades

- Listagem de ações cadastradas
- Adição de novas ações
- Remoção de ações
- Cálculo automático:
  - Valor atual da ação (via lógica back-end)
  - Valor total investido
  - Valorização percentual desde a compra

## Tecnologias utilizadas

- [Flask](https://flask.palletsprojects.com/)
- [Flask-OpenAPI3](https://pypi.org/project/flask-openapi3/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLite](https://www.sqlite.org/)

## Instalação e execução

Clone o repositório:
```bash
git clone https://github.com/cclguedes/Carteira_Acoes_API_Backend
```
Entre na pasta do projeto:
```bash
cd carteira_acoes_api_backend
```
Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
```
```bash
source venv/bin/activate # Linux/macOS
```
```bash
venv\Scripts\activate # Windows
```
Entre na pasta:
```bash
cd carteira_acoes_api_backend
```
Instale as dependências:
```bash
pip install -r requirements.txt
```
Execute o servidor:
```bash
flask run --host 0.0.0.0 --port 5000
```
## Sobre o autor

Sou Caio Guedes, engenheiro eletricista e especialista em gestão de projetos, trabalhando atualmente como Product Owner de projetos de tecnologia na indústria audiovisual. No momento, busco conhecimento mais profundo em arquitetura de softwares e desenvolvimento de sistemas para o aprimoramento das minhas atividades na gestão de projetos ágeis.