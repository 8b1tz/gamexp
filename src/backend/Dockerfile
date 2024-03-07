FROM python:3.9-alpine

# Instalar as dependências de compilação do SQLite
RUN apk add --no-cache gcc musl-dev sqlite-dev

WORKDIR /src

COPY ./app /src/app

COPY requirements.txt /src

RUN pip install -r requirements.txt

RUN python -c 'from app.controllers.controller import create_table, create_tokens_table; create_table(); create_tokens_table()'
