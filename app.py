import sqlite3

conn = sqlite3.connect('Movies.db')



cursor = conn.cursor()

# Create the movies table







# Select all movies

cursor.execute('SELECT * FROM movies')

all_movies = cursor.fetchall()

print("All movies:")

for movie in all_movies:

    print(movie)



# Select movies after 2000

cursor.execute('SELECT title, year FROM movies WHERE year > 1900')

recent_movies = cursor.fetchall()

print("\nMovies after 1900:")

for movie in recent_movies:

    print(f"{movie[0]} ({movie[1]})")



# Select average rating

cursor.execute('SELECT AVG(rating) FROM movies')

avg_rating = cursor.fetchone()[0]

print(f"\nAverage rating: {avg_rating:.2f}")

# Update the rating of a movie

cursor.execute('''

UPDATE movies

SET year = 2014

WHERE title = 'epic'

''')

cursor.execute('DELETE FROM movies WHERE title = "Pulp Fiction"')
conn.commit()
conn.close()