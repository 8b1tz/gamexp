from fastapi import FastAPI, HTTPException
from app.controllers.controller import get_games, get_game_by_id, get_games_by_category, get_games_by_platform, get_games_by_publisher, get_games_by_developer, get_categories, get_developers, get_plataforms, get_publishers, get_game_by_release_year

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to the homepage"}


@app.get('/api/games')
def games():
    return get_games()


@app.get('/api/game/{game_id}')
def game(game_id: int):
    return get_game_by_id(game_id)


@app.get('/api/games/category/{category}')
def games_by_category(category: str):
    return get_games_by_category(category)


@app.get('/api/games/platform/{platform}')
def games_by_platform(platform: str):
    return get_games_by_platform(platform)


@app.get('/api/games/publisher/{publisher}')
def games_by_publisher(publisher: str):
    return get_games_by_publisher(publisher)


@app.get('/api/games/developer/{developer}')
def games_by_developer(developer: str):
    return get_games_by_developer(developer)


@app.get('/api/games/{year}')
def game_by_release_year(year: str):
    return get_game_by_release_year(year)


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
