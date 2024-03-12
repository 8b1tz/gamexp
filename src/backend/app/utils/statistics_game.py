import pandas as pd
from app.controllers.controller import get_games
from numpy import round


def games_per_publishers():
    response = get_games()
    df = pd.DataFrame(response)
    publishers_counts = df['publisher'].value_counts()
    publishers_counts_dict = publishers_counts.to_dict()
    return publishers_counts_dict


def year_with_most_releases():
    response = get_games()
    df = pd.DataFrame(response)
    df['release_date'] = pd.to_datetime(df['release_date'],
                                        format="%Y-%m-%d",
                                        errors='coerce')
    df['release_year'] = df['release_date'].apply(lambda x: x.year
                                                  if pd.notnull(x) else None)
    year_with_most_releases = df['release_year'].value_counts().idxmax()
    return year_with_most_releases


def games_per_genre():
    response = get_games()
    df = pd.DataFrame(response)
    genre_counts = df['genre'].value_counts()
    total_jogos = genre_counts.sum()
    genre_percentages = (genre_counts / total_jogos) * 100
    genre_percentages_rounded = round(genre_percentages, decimals=2)
    genre_percentage_dict = dict(zip(genre_percentages_rounded.index,
                                     genre_percentages_rounded.values))
    return genre_percentage_dict
