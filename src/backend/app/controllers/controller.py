import requests
import sqlite3
import hashlib
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
import jwt

def get_games():
    url = "https://www.freetogame.com/api/games"
    response = requests.get(url)
    
    if response.status_code == 200:
        games = response.json()
        return games
    else:
        return 'Erro na API'

def get_game_by_id(game_id: int):
    url = f"https://www.freetogame.com/api/game?id={game_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        game = response.json()
        return game
    else:
        return 'Erro na API'
        
def get_game_by_category(category: str):
    pass

def get_game_by_plataform(plataform: str):
    pass

def get_game_by_publish():
    pass

def get_game_by_developer():
    pass

def get_categorys():
    pass