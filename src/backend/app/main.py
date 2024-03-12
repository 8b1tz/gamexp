from typing import Dict, List

from app.controllers.controller import (filter_games, get_categories,
                                        get_developers, get_game_by_id,
                                        get_games, get_platforms,
                                        get_publishers)
from app.utils.statistics_game import (games_per_genre, games_per_publishers,
                                       year_with_most_releases)
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Welcome to the homepage"}


@app.get('/api/game')
def game(
    year: int = None,
    developer: str = None,
    publisher: str = None,
    category: str = None,
    platform: str = None
) -> List[Dict]:
    return filter_games(year, developer, publisher, category, platform)


@app.get('/api/game/{id}')
def game_by_id(id):
    return get_game_by_id(id)


@app.get('/api/games')
def games():
    return get_games()


@app.get('/api/categories')
def categories():
    return get_categories()


@app.get('/api/publishers')
def publishers():
    return get_publishers()


@app.get('/api/platforms')
def platforms():
    return get_platforms()


@app.get('/api/developers')
def developers():
    return get_developers()


@app.get('/api/statistics')
def statistics():
    return {'games_per_genre': games_per_genre(),
            'games_per_publishers': games_per_publishers(),
            'year_with_most_releases': year_with_most_releases()
            }


@app.exception_handler(404)
async def page_not_found(request, exc):
    return {"message": "Page not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
