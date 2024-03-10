import requests
from app.controllers.controller import (get_categories, get_developers,
                                        get_game_by_id,
                                        get_game_by_release_year, get_games,
                                        get_games_by_category,
                                        get_games_by_developer,
                                        get_games_by_platform,
                                        get_games_by_publisher, get_plataforms,
                                        get_publishers)
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Welcome to the homepage"}


@app.get('/api/game')
def game_tag(
    year: int = None,
    developer: str = None,
    publisher: str = None,
    category: str = None,
    platform: str = None
):
    params = {}
    
    if year:
        params['year'] = year
    if developer:
        params['developer'] = developer
    if publisher:
        params['publisher'] = publisher
    if category:
        params['category'] = category
    if platform:
        params['platform'] = platform

    return make_api_request('games', params=params)


def make_api_request(endpoint: str, params: dict = None):
    url = f"https://www.freetogame.com/api/{endpoint}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f'Erro na API: {response.status_code}'


@app.get('/api/games')
def games():
    return get_games()


@app.get('/api/categories')
def categories():
    return get_categories()


@app.get('/api/publishers')
def publishers():
    return get_publishers()


@app.get('/api/plataforms')
def plataforms():
    return get_plataforms()


@app.get('/api/developers')
def developers():
    return get_developers()


@app.exception_handler(404)
async def page_not_found(request, exc):
    return {"message": "Page not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
