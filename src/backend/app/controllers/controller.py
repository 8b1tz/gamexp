import requests
from datetime import datetime


def create_no_duplicate_sequence(key):
    all_games = get_games()
    return {game[key] for game in all_games}


def make_api_request(endpoint: str, params: dict = None):
    url = f"https://www.freetogame.com/api/{endpoint}"
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f'Erro na API: {response.status_code}'


def get_games():
    return make_api_request('games')


def get_game_by_id(game_id: int):
    return make_api_request(f'game?id={game_id}')


def get_games_by_category(category: str):
    return make_api_request('games', params={'  ': category})


def get_games_by_platform(platform: str):
    return make_api_request('games', params={'platform': platform})


def get_games_by_publisher(publisher: str):
    return make_api_request('games', params={'publisher': publisher})


def get_games_by_developer(developer: str):
    return make_api_request('games', params={'developer': developer})


def get_game_by_release_year(year_str):
    all_games = get_games()
    try:
        year = int(year_str)
    except ValueError:
        print("Ano inválido. Deve ser um número inteiro.")
        return None

    filtered_games = []
    for game in all_games:
        try:
            game_date = datetime.strptime(game.get('release_date'), '%Y-%m-%d').date()
            if game_date.year == year:
                filtered_games.append(game)
        except ValueError:
            print(f"Ignorando data inválida: {game.get('release_date')}")

    if filtered_games:
        return filtered_games
    else:
        return None


def get_categories():
    categories = create_no_duplicate_sequence('genre')
    return categories


def get_publishers():
    publishers = create_no_duplicate_sequence('publisher')
    return publishers


def get_plataforms():
    publishers = create_no_duplicate_sequence('platform')
    return publishers


def get_developers():
    publishers = create_no_duplicate_sequence('developer')
    return publishers
