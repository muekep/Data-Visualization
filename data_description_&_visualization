#Import the necessary libraries to analyse the data
import pandas as pd
import numpy as np
#Load the data to the python environment
Netflix_shows_movies = pd.read_csv('C:/Users/Paul/Nexford/Netflix_Shows_Movies.csv')
Netflix_shows_movies
#Have a glimpe at the info about each column of the data
print(Netflix_shows_movies.info())
#A summary of the missing values in each column
print(Netflix_shows_movies.isnull().sum())
#To adress missing values, I drop rowa with missing values since the data is a of string type
Netflix_shows_movies = Netflix_shows_movies.dropna()
print(Netflix_shows_movies.info())
#Describing the data
#showing the first 10 rows
Netflix_shows_movies.head(10)
#showing the last 10 rows
Netflix_shows_movies.tail(10)
#The shape of the data
Netflix_shows_movies.shape
#Getting info about datatype,non null counts and memory
Netflix_shows_movies.info()
#Summary statistics for numerical columns
Netflix_shows_movies.describe()
#Summary statistics for categorical columns
Netflix_shows_movies.describe(include=['object'])
import datetime
Netflix_shows_movies=pd.to_datetime(Netflix_shows_movies, 'listed_in', format='%m/%d/%Y')
#Calculate the mean, median, and standard deviation of a column
print("Mean:", Netflix_shows_movies['release_year'].mean())
print("Median:", Netflix_shows_movies['duration'].median())
print("Standard Deviation:", Netflix_shows_movies['listed_in'].std())

#import the data visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
#Bar Graph with seaborn
plt.figure(figsize=(8, 6))  # Adjust figure size if needed
sns.countplot(x='type', data=Netflix_shows_movies)
plt.title('Seaborn Bar Chart of Categories')
plt.xlabel('Category') #labeling the x axis
plt.ylabel('Count') #labeling the y axis
plt.show()
#Bar graph with matplotlib
category_counts = Netflix_shows_movies['type'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(category_counts.index, category_counts.values)
plt.title('Matplotlib Bar Chart of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
# Bar graph with plotly library
fig=px.bar(Netflix_shows_movies, x='type', title='Plotly Express Bar Chart of Categories')
fig.show()

import plotly.graph_objects as go
category_counts = Netflix_shows_movies['type'].value_counts().reset_index()
category_counts.columns = ['type', 'Count'] #Rename the columns to something more readable.

fig = go.Figure(data=[go.Bar(x=category_counts['type'], y=category_counts['Count'])])

fig.update_layout(title='Plotly Go Bar Chart of Categories',
                  xaxis_title='Category',
                  yaxis_title='Count')

fig.show()

plt.figure(figsize=(8, 6))
sns.countplot(y='rating', hue='type', data=Netflix_shows_movies)
plt.title('Seaborn Countplot: Rating vs Type')
plt.show()

cross_tab = pd.crosstab(Netflix_shows_movies['rating'], Netflix_shows_movies['type'])
cross_tab.plot(kind='bar', stacked=False, figsize=(8, 6))
plt.title('Matplotlib Grouped Bar Chart: rating vs Category2')
plt.xlabel('Category1')
plt.ylabel('Count')
plt.show()

fig = px.histogram(df, x='rating', color='type',
                   title='Plotly Express Grouped Bar Chart: Rating vs Type')
fig.show()
