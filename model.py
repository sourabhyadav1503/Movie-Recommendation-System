import pandas as pd

# Load movie data
movies = pd.read_csv("Movies.csv")
print(movies.columns)
print(movies.head())
def recommend(movie_name):
    movie_name = movie_name.lower()

    movie = movies[movies["movie"].str.lower() == movie_name]

    if movie.empty:
        return ["Movie not found!"]

    genre = movie.iloc[0]["genre"]

    recommendations = movies[
        (movies["genre"] == genre) &
        (movies["movie"].str.lower() != movie_name)
    ]

    return recommendations["movie"].tolist()