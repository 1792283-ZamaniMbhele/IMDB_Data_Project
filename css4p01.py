# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 08:25:03 2024

@author: A0063097
"""

import pandas as pd 

df = pd.read_csv("movie_dataset.csv")

#Cleaning data set, filling empty cells with average value
metascore_mean = df['Metascore'].mean()
df['Metascore'].fillna(metascore_mean, inplace = True)
pd.set_option('display.max_rows', None)
print (df.head())
print("The metascore mean is: ", metascore_mean)

revenue_mean = df['Revenue (Millions)'].mean()
df['Revenue (Millions)'].fillna(revenue_mean, inplace = True)
print("The revenue mean is: ", revenue_mean)

# What is the highest rated movie in the dataset?
highest_rated_movie_index = df['Rating'].idxmax()
highest_rated_movie = df.loc[highest_rated_movie_index]
print("The highest rated movie is:", highest_rated_movie)

# What is the average revenue of all movies in the dataset? 
avg_revenue_all = df['Revenue (Millions)'].mean()
print("The average revenue for all movies is: ", avg_revenue_all)

# What is the average revenue of movies from 2015 to 2017 in the dataset?
rev_between_years = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]
average_rev = rev_between_years['Revenue (Millions)'].mean()
print("The average revenue revenue between 2015 and 2017 is: ", average_rev)

# How many movies were released in the year 2016?
release_year = df.sort_values('Year')
release_year = len(df[df.Year == 2016])
print("The number of movies released in 2016 is:", release_year)


# How many movies were directed by Christopher Nolan?
nolan_movies_count = len(df[df.Director == "Christopher Nolan"])
print("Christopher Nolan directed:", nolan_movies_count)

# How many movies in the dataset have a rating of at least 8.0?
high_rated_movies = len(df[df.Rating >= 8.0])
print("Movies with the rating of at least 8.0 are: ", high_rated_movies)

# What is the median rating of movies directed by Christopher Nolan?
nolan_movies  = df[df['Director'] == 'Christopher Nolan']
median_rating_nolan = nolan_movies['Rating'].median()
print("The median rating of movies directed by Christopher Nolan is:", median_rating_nolan)

#  The year with the highest average rating

highest_ave_rating = df.groupby('Year')['Rating'].max().idxmax()
print("The highest average rating per year is:", highest_ave_rating)

# The percentage increase in number of movies made between 2006 and 2016?

# Filter movies made in 2006 and 2016
movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]

# Count the number of movies for each year
count_2006 = len(movies_2006)
count_2016 = len(movies_2016)

# The percentage increase in number of movies made between 2006 and 2016?

percentage_increase = ((count_2016 - count_2006) / count_2006) * 100

print(f"Number of movies in 2006: {count_2006}")
print(f"Number of movies in 2016: {count_2016}")
print(f"Percentage Increase in number of movies made between 2006 and 2016: {percentage_increase:.2f}%")


#Find the most common actor in all the movies?
from collections import Counter

# Combine all actors from the "Actors" column into a single list
all_actors = [actor.strip() for actors in df['Actors'] for actor in actors.split(',')]

actor_counts = Counter(all_actors)

most_common_actor, count = actor_counts.most_common(1)[0]

print("Most Common Actor:", most_common_actor)
print("Count:", count)





# How many unique genres are there in the dataset?

unique_genres = set()

# Split values in 'Genre' column by commas and add each genre to the set
for value in df['Genre']:
    genres = value.split(',')
    for genre in genres:
        unique_genres.add(genre.strip())  # Use strip() to remove leading/trailing whitespaces

print("Unique Genres:", unique_genres)
print("Number of Unique Genres:", len(unique_genres))
            
# Correlation of the numerical features, what insights can you deduce? Mention at least 5 insights
numerical_features = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numerical_features.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Extracting insights
insight_1 = "There is a strong positive correlation between X and Y."
insight_2 = "Feature Z has a negative correlation with both A and B."
insight_3 = "No significant correlation is observed between P and Q."
insight_4 = "A strong correlation exists between R and S, indicating potential multicollinearity."
insight_5 = "Feature T shows a moderate positive correlation with U."

print("\nInsights:")
print(insight_1)
print(insight_2)
print(insight_3)
print(insight_4)
print(insight_5)
    



