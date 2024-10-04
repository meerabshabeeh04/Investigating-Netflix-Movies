import pandas as pd  # Import pandas for data manipulation
import matplotlib.pyplot as plt  # Import matplotlib for data visualization
# Load Netflix dataset from CSV file into a pandas DataFrame
netflix_df = pd.read_csv('Investigating Netflix Movies/netflix_data.csv')
# Filter the dataset to include only movies
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']
# Select specific columns relevant to the analysis: title, country, genre, release year, and duration
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]
# Filter movies with a duration of less than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]
# Initialize an empty list to store color labels for the scatter plot
colors = []
# Iterate through the DataFrame rows to assign colors based on the genre of each movie
for lab, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':  # If the genre is 'Children', color the point Blue
        colors.append('Blue')
    elif row['genre'] == 'Documentaries':  # If the genre is 'Documentaries', color the point Black
        colors.append('Black')
    elif row['genre'] == 'Stand-Up':  # If the genre is 'Stand-Up', color the point Red
        colors.append('Red')
    else:  # For all other genres, color the point Green
        colors.append('Green')
# Create a figure for the plot with specified size
fig = plt.figure(figsize=(12, 8))
# Create a scatter plot of movie release year vs. duration, with colors based on genre
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
# Label the x-axis as 'Release year'
plt.xlabel('Release year')
# Label the y-axis as 'Duration (min)'
plt.ylabel('Duration (min)')
# Set the title of the scatter plot
plt.title('Movie Duration by Year of Release')
# Display the plot
plt.show()