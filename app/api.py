from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Welcome to the homepage"}

@app.get('/movies')
def movies():
    return {"message": "List of movies"}

@app.get('/movie/{movie_id}')
def movie(movie_id: int):
    return {"message": f"Movie details for movie {movie_id}"}

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
