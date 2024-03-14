# Projeto FastAPI + Vue

## Visão Geral

Este projeto tem como objetivo desenvolver um aplicativo web moderno utilizando FastAPI para o backend e Vue para o frontend. O backend será desenvolvido por [8b1tz](https://github.com/8b1tz), enquanto o frontend será desenvolvido por [AnaLinsDev](https://github.com/AnaLinsDev).

## Tecnologias Utilizadas

- **FastAPI**: Um framework moderno e rápido para construir APIs com Python.
- **Python**: Linguagem de programação utilizada para o backend.
- **Pandas**: Biblioteca para manipulação e análise de dados em Python.
- **NumPy**: Biblioteca para computação numérica em Python.
- **Vue**: Biblioteca JavaScript para a construção de interfaces de usuário.

## Funcionalidades

O aplicativo terá as seguintes funcionalidades:

- Registro e autenticação de usuários.
- CRUD (Create, Read, Update, Delete) para diferentes entidades.
- Docker: Utilização de contêineres para facilitar a implantação e o gerenciamento do ambiente de desenvolvimento.
- Criação de estatísticas relevantes.
- Interação entre o frontend e o backend por meio de requisições HTTP.

## Desenvolvedores

- **Backend**: [8b1tz](https://github.com/8b1tz)
- **Frontend**: [AnaLinsDev](https://github.com/AnaLinsDev)

## Estrutura do Projeto

O projeto seguirá uma estrutura básica:

```
src/
│
├── backend/
│   ├── app/
│   │   ├── controllers/       
│   │   │   └── controller.py 
│   │   ├── utils/              
│   │   │   └── statistics.py
│   │   └── __init__.py         
│   ├── main.py                 
│   └── dockerfile             
│
├── frontend/
│   ├── assets/                 
│   ├── components/             
│   ├── layouts/               
│   ├── pages/                  
│   ├── static/                
│   ├── store/                  
│   └── dockerfile              
│
└── docker-compose.yaml         

```

Como executar:

1. **Clone o repositório:**

```git clone https://github.com/8b1tz/gamexp```

2. **Abra o projeto no seu editor de código.**

3. **Navegue até a pasta `src`:**

```cd gamexp/src```

4. **Construa a imagem usando o arquivo `docker-compose.yaml` (verifique se o Docker está em execução):**

```docker-compose build```

5. **Execute o contêiner com a imagem criada:**

```docker-compose up -d```

### Telas:

#### /home
<img src="https://github.com/8b1tz/gamexp/assets/53948477/b6bde87b-633f-4296-91c0-ef1d0f808cfb" width="500">

- A tela /home representa a página inicial do aplicativo, onde os usuários são recebidos ao acessar a plataforma. Esta tela pode incluir informações sobre o aplicativo, destaques de recursos ou uma visão geral dos últimos jogos adicionados.

#### /games 
<img src="https://github.com/8b1tz/gamexp/assets/53948477/d893bfdf-f0c6-43b8-9e91-fd1106234cd7" width="500">

- A tela /games exibe uma lista de jogos disponíveis no aplicativo. Os usuários podem explorar e descobrir novos jogos nesta página. Dependendo da implementação, pode haver opções de filtro ou ordenação para ajudar os usuários a encontrar os jogos desejados.

#### /game/filter 
<img src="https://github.com/8b1tz/gamexp/assets/53948477/a12d7992-71c3-4b85-8d3d-f0c9c8d9920e" width="500">

- A tela /game/filter permite que os usuários filtrem os jogos com base em diferentes critérios, como gênero, classificação etária ou popularidade. Essa funcionalidade pode ajudar os usuários a refinar sua busca e encontrar jogos específicos que atendam às suas preferências.

#### /game/{id}
<img src="https://github.com/8b1tz/gamexp/assets/53948477/52c02c51-9783-497d-996c-5861c45131d1" width="500">

- A tela /game/{id} exibe informações detalhadas sobre um jogo específico, identificado pelo seu ID. Os usuários podem encontrar detalhes como título do jogo, descrição, classificação, avaliações dos usuários e possivelmente capturas de tela ou vídeos do jogo.

#### /dashboard (Fase de criação)

- A tela /dashboard exibe estatísticas relevantes gerais dos jogos.

Este projeto seguirá uma abordagem de desenvolvimento colaborativo, com o backend e o frontend trabalhando em conjunto para criar uma aplicação coesa e eficiente. Fique à vontade para contribuir ou fornecer feedback!
