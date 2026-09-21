# CODSOFT AI Internship
# Task 4: Recommendation System

movies = {
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Titanic": ["Romance", "Drama"],
    "Avengers": ["Action", "Adventure", "Sci-Fi"],
    "The Notebook": ["Romance", "Drama"],
    "Jurassic Park": ["Adventure", "Sci-Fi", "Thriller"],
    "Toy Story": ["Animation", "Comedy", "Adventure"]
}


def recommend_movies(user_preference):
    recommendations = []

    for movie, genres in movies.items():
        if user_preference.lower() in [genre.lower() for genre in genres]:
            recommendations.append(movie)

    return recommendations


print("================================")
print("     Movie Recommendation System")
print("================================")

print("\nAvailable genres:")
print("Action, Sci-Fi, Drama, Romance, Adventure, Thriller,")
print("Crime, Animation, Comedy")

preference = input("\nEnter your preferred genre: ")

recommendations = recommend_movies(preference)

if recommendations:
    print("\nRecommended Movies:")
    for movie in recommendations:
        print("-", movie)
else:
    print("\nSorry, no movies found for this genre.")
