import hashlib
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.controllers.controller import oauth2_scheme, get_games, get_game_by_id, get_current_user, revoke_token, login, create_user, get_user_by_username, get_access_token, is_token_revoked

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to the homepage"}

@app.get('/games')
def games():
    return get_games()

@app.get('/game/{game_id}')
def game(game_id: int):
    return get_game_by_id(game_id)

@app.exception_handler(404)
async def page_not_found(request, exc):
    return {"message": "Page not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
