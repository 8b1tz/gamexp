import requests
import sqlite3
import hashlib

def connect_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    return conn, c

def create_table():
    conn, c = connect_db()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    email TEXT UNIQUE,
                    password TEXT
                )''')
    conn.commit()
    conn.close()

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

def get_users():
    conn, c = connect_db()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users

def get_user_by_username(username: str):
    conn, c = connect_db()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user

def get_user_by_email(email: str):
    conn, c = connect_db()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    user = c.fetchone()
    conn.close()
    return user

def create_user(username: str, email: str, password: str):
    conn, c = connect_db()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
              (username, email, hashed_password))
    conn.commit()
    conn.close()

def login(username: str, password: str):
    user = get_user_by_username(username)
    if user:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if user[3] == hashed_password:
            return True
    return False

# def get_comments_by_game_id(game_id: int):
#     pass

# def get_ratings_by_game_id(game_id: int):
#     pass

# def add_comment(user_id: int, game_id: int, comment: str):
#     pass

# def add_rating(user_id: int, game_id: int, rating: int):
#     pass
