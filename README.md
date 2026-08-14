
# Agenda

Sistema web de gerenciamento de eventos desenvolvido com Django.
A aplicação permite criar, visualizar, editar e excluir eventos, organizando-os por data e horário.


## 1. Sobre o projeto

O Agenda foi desenvolvido coomo um projeto de estudo para praticar desenvolvimento web com Python e Django.


### Funcionalidades atuais

- Criar eventos
- Visualizar detalhes dos eventos
- Editar eventos
- Excluir eventos
- Ordenar eventos por data e horário
- Interface utilizando Bootstrap
- Banco de dados SQLite

## 2. Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML 5
- CSS3
- Bootstrap 5

## 3.  Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`.

Para instalar:

```bash
pip install -r requirements.txt
```

## 4. Como rodar a aplicação

Clone o repositório:

```bash
git clone https://github.com/pedrooivann/agenda-django
```

Entre na pasta do projeto:

```bash
cd agenda-django
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrations:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```