# Flask REST API

> Projeto desenvolvido no Bootcamp Desenvolvedor Full Stack Python. API REST com Flask para gerenciamento de informações de desenvolvedores (nome e habilidades), com exemplos progressivos desde "Hello World" até CRUD completo.

<div align="center">

</div>
<br>
<div align="center">
<img src="https://img.shields.io/github/release-date/henriquemap/flask-rest-api">
</div>
<br>
<div align="center">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/henriquemap/flask-rest-api">
<img src="https://img.shields.io/github/issues/henriquemap/flask-rest-api">
</div>
<br>
<div align="center">
<img src="https://img.shields.io/github/forks/henriquemap/flask-rest-api?style=flat">
<img src="https://img.shields.io/github/stars/henriquemap/flask-rest-api?style=flat">
</div>
<div align="center">
<br>
</div>

## 📋 Sobre o Projeto

Este repositório contém o material e os códigos da aula de **Framework Flask e REST API**, ministrada por [Rafael Galeani](https://github.com/rafegal). Inclui uma API que gerencia informações de desenvolvedores (nome e habilidades), com exemplos em três níveis: introdução ao Flask, API de testes e API de desenvolvedores com operações GET, POST, PUT e DELETE.

## 📁 Estrutura do Projeto

### Olá Flask (`ola_flask/`)
- **run.py** — Exemplo mínimo "Hello World" com Flask; primeira rota e execução do servidor.

### Primeira API (`primeira_api/`)
- **app.py** — Modelo de API para testes: rota com parâmetro (id), uso de `jsonify` e `request`, exemplo de soma via POST.

### API de Desenvolvedores (`dev_api/`)
- **app.py** — API principal: listagem e inclusão de desenvolvedores (GET/POST em `/dev/`), consulta, alteração e exclusão por ID (GET/PUT/DELETE em `/dev/<id>/`).

### Documentação (raiz do repositório)
- **theory.md** — Conceitos de API, REST, REST API, métodos HTTP, JSON e Flask.
- **configuration-steps.md** — Passo a passo: PIP, ambiente virtual, instalação do Flask e uso do Postman.
- **challenges.md** — Desafios propostos (ex.: API de cadastro de tarefas).

## 📂 Estrutura do repositório

```
README.md
requirements.txt
theory.md
configuration-steps.md
challenges.md
ola_flask/
    run.py                 # Hello World Flask
primeira_api/
    app.py                 # API de testes (jsonify, request, soma)
dev_api/
    app.py                 # API de desenvolvedores (CRUD)
```

## 🛠️ Tecnologias Utilizadas

- **Python** — Linguagem de programação
- **Flask** — Framework web para criação da API
- **JSON** — Formato de dados da API
- **Postman** — Ferramenta para testar requisições HTTP (GET, POST, PUT, DELETE)

## 📝 Funcionalidades Principais

### API de Desenvolvedores (`dev_api`)
- **GET /dev/** — Listar todos os desenvolvedores
- **POST /dev/** — Incluir novo desenvolvedor (nome e habilidades)
- **GET /dev/<id>/** — Consultar desenvolvedor por ID
- **PUT /dev/<id>/** — Alterar desenvolvedor por ID
- **DELETE /dev/<id>/** — Excluir desenvolvedor por ID (tratamento de erros e mensagens de status)

### Primeira API (`primeira_api`)
- Resposta JSON com parâmetro de rota e exemplo de soma via POST.

### Olá Flask (`ola_flask`)
- Rota raiz retornando "Hello World".

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7+
- pip

### Instalação das dependências

```bash
pip install -r requirements.txt
```

### Criação do ambiente virtual (recomendado)

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Executando cada aplicação

**Olá Flask:**

```bash
cd ola_flask
python run.py
# Acesse: http://127.0.0.1:5000/
```

**Primeira API:**

```bash
cd primeira_api
python app.py
# Rotas: http://127.0.0.1:5000/<id> e http://127.0.0.1:5000/soma (POST)
```

**API de Desenvolvedores:**

```bash
cd dev_api
python app.py
# Base URL: http://127.0.0.1:5000/dev/
```

Use o **Postman** (ou similar) para testar os métodos GET, POST, PUT e DELETE nas rotas indicadas.

## 📚 Conteúdos Abordados

- ✅ Conceitos de API, REST e REST API
- ✅ Métodos HTTP (GET, POST, PUT, DELETE)
- ✅ Uso de `jsonify` e `request` no Flask
- ✅ Decoradores e rotas com parâmetros
- ✅ Testes de API com Postman
- ✅ Estrutura de respostas JSON e tratamento de erros

## ⚙️ Como Funciona

### API de Desenvolvedores
1. Os dados são mantidos em uma lista em memória (`desenvolvedores`) com campos: `id`, `nome`, `habilidades`.
2. **GET /dev/** retorna a lista completa em JSON.
3. **POST /dev/** recebe JSON no body, atribui um `id` sequencial e adiciona à lista.
4. **GET /dev/<id>/** retorna o desenvolvedor na posição `id` ou mensagem de erro se não existir.
5. **PUT /dev/<id>/** substitui o registro na posição `id` pelos dados enviados no body.
6. **DELETE /dev/<id>/** remove o registro na posição `id` e retorna confirmação.

### Documentação adicional
- **[Teoria](theory.md)** — Detalhamento dos conceitos (API, REST, HTTP, JSON, Flask).
- **[Configuração](configuration-steps.md)** — PIP, ambiente virtual, Flask e Postman.
- **[Desafios](challenges.md)** — Desafios propostos (ex.: API de tarefas).

**Status dos desafios: 0 / 4**

## 📄 Licença

Este projeto não possui arquivo de licença definido. Para uso educacional no contexto do Bootcamp Desenvolvedor Full Stack Python.

## 📖 Referências

- Código-fonte em `ola_flask/`, `primeira_api/` e `dev_api/`
- Documentação do [Flask](https://flask.palletsprojects.com/)
- Material da aula — Bootcamp Desenvolvedor Full Stack Python (Rafael Galeani)

---

### Hashtags

#Python #Flask #RESTAPI #Backend #APIREST #JSON #Postman #Bootcamp #FullStack #WebDevelopment #OpenSource #GitHub #CodeExamples #Learning #Developer

### Meta Keywords

```
Python, Flask, REST API, API REST, JSON, Postman, Bootcamp Full Stack,
desenvolvedor Python, backend, métodos HTTP, GET POST PUT DELETE,
CRUD, integração de APIs, código aberto
```

<br>
<div align="center">
  <a href="https://ko-fi.com/henriquematheus" target="_blank">
    <img src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" alt="Buy Me a Coffee at ko-fi.com" width="200" />
  </a>
</div>

____

**Desenvolvido por Henrique Matheus Alves Pereira**

*Editor: Visual Studio Code | Tema: Monokai Pro | Extensões: Error Lens, Git Lens, Python*
