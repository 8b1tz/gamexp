from fastapi import FastAPI, HTTPException
from app.controllers.controller import get_users, get_games, get_game_by_id

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

@app.get('/profile')
def profile():
    return {"message": "User profile page"}

@app.post('/login')
def login():
    return {"message": "Login successful"}

@app.post('/register')
def register():
    return {"message": "Registration successful"}

@app.get('/logout')
def logout():
    return {"message": "Logout successful"}

@app.exception_handler(404)
async def page_not_found(request, exc):
    return {"message": "Page not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
