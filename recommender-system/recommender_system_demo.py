import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.DataFrame({
    "user": ["A", "A", "A", "B", "B", "C", "C", "D", "D", "D"],
    "movie": ["Movie 1", "Movie 2", "Movie 3", "Movie 1", "Movie 3", "Movie 2", "Movie 4", "Movie 1", "Movie 3", "Movie 4"],
    "rating": [5, 4, 3, 4, 5, 5, 4, 3, 4, 5]
})

matrix = ratings.pivot_table(index="user", columns="movie", values="rating").fillna(0)
item_similarity = cosine_similarity(matrix.T)
similarity_df = pd.DataFrame(item_similarity, index=matrix.columns, columns=matrix.columns)

target_movie = "Movie 1"
recommendations = similarity_df[target_movie].sort_values(ascending=False).drop(target_movie)

print("Recommender System Demo")
print(f"Movies similar to {target_movie}:")
print(recommendations)
