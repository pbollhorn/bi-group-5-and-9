import sys
sys.path.append("..")

import pandas as pd
import ast  # Abstract Syntax Trees - safely parse string list to Python list
import seaborn as sns
import matplotlib.pyplot as plt
from reader import generic_reader

movies = generic_reader.read_csv_file_to_data_frame("movie_data/movies.csv")
print(movies.info())
movies


columns_to_keep = ['budget', 'movie_id', 'original_title', 'overview', 'release_date', 'revenue', 'runtime', 'vote_average', 'vote_count', 'director_person_ids', 'genre_ids', 'collection_id', 'cast_person_ids', 'cast_credit_ids', 'crew_person_ids', 'crew_credit_ids']
df_movies = movies[columns_to_keep].copy()

df_movies['genre_ids'] = movies['genre_ids'].apply(ast.literal_eval)
df_movies['cast_person_ids'] = movies['cast_person_ids'].apply(ast.literal_eval)
df_movies['crew_person_ids'] = movies['crew_person_ids'].apply(ast.literal_eval)
df_movies['director_person_ids'] = movies['director_person_ids'].apply(ast.literal_eval)
df_movies['release_date'] = pd.to_datetime(movies['release_date'])


df_movies = df_movies[(df_movies['budget'] != 0) & (df_movies['revenue'] != 0)].copy()

df_persons = generic_reader.read_csv_file_to_data_frame("movie_data/persons.csv")
print(df_persons.info())
df_persons

columns_to_keep = ['birthday', 'deathday', 'gender', 'person_id', 'known_for_department']
df_persons = df_persons[columns_to_keep].copy()
df_persons['birthday'] = pd.to_datetime(df_persons['birthday'])
df_persons['deathday'] = pd.to_datetime(df_persons['deathday'])
df_persons

df_persons['birthday'] = pd.to_datetime(df_persons['birthday'], errors='coerce')
df_persons['deathday'] = pd.to_datetime(df_persons['deathday'], errors='coerce')

birthday_nat_count = df_persons['birthday'].isna().sum()

print(f"'NaT' in 'birthday' column: {birthday_nat_count}")

df_persons = df_persons[pd.notna(df_persons['birthday'])].copy()

def calculate_age_from_row(row):
    birthday = row['birthday']
    deathday = row['deathday']
    
    if pd.isna(deathday):
        end_date = pd.to_datetime('2023-12-31')
    else:
        end_date = deathday
    
    age = end_date.year - birthday.year - ((end_date.month, end_date.day) < (birthday.month, birthday.day))
    return age


df_persons['age'] = df_persons.apply(calculate_age_from_row, axis=1)
df_persons.sort_values(by="age", ascending=False)


cast_counts = df_movies[['cast_person_ids']].explode('cast_person_ids')
director_counts = df_movies[['director_person_ids']].explode('director_person_ids')

cast_counts = cast_counts.rename(columns={'cast_person_ids': 'person_id'})
director_counts = director_counts.rename(columns={'director_person_ids': 'person_id'})

all_counts = pd.concat([cast_counts, director_counts], ignore_index=True)

person_movie_count = all_counts['person_id'].value_counts()

df_persons['movie_count'] = df_persons['person_id'].map(person_movie_count).fillna(0).astype(int)

df_persons = df_persons[(df_persons['movie_count'] != 0)].copy()

df_movies_first = df_movies.copy()

# Replace list columns with just the first element and rename
df_movies_first['cast_person_id'] = df_movies_first['cast_person_ids'].str[0].astype('Int64')
df_movies_first['director_person_id'] = df_movies_first['director_person_ids'].str[0].astype('Int64')

# Drop the old list columns if you don’t need them anymore
df_movies_first = df_movies_first.drop(columns=['cast_person_ids', 'director_person_ids'])

#print(df_movies_first[['cast_person_id', 'director_person_id']].head())

df_persons_first = df_persons.copy()

# Merge df_movies_first with df_persons on cast_person_id = person_id
df_movies_cast = df_movies_first.merge(
    df_persons_first,
    left_on="cast_person_id",
    right_on="person_id",
    how="left",
    suffixes=("", "_cast")
)

# Show result
df_movies_cast.head()

# Calculate age at release
df_movies_cast['age_at_release'] = df_movies_cast.apply(
    lambda row: row['release_date'].year - row['birthday'].year - 
                ((row['release_date'].month, row['release_date'].day) < (row['birthday'].month, row['birthday'].day)),
    axis=1
)

# Check
df_movies_cast[['original_title', 'release_date', 'birthday', 'age_at_release']].head()


import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

df_movies_cast['gender_filled'] = df_movies_cast['gender'].fillna(0)

# Map gender codes to colors
gender_colors = {
    0: 'gray',    # unknown
    1: 'red',     # female
    2: 'blue',    # male
    3: 'green'    # non-binary
}
df_movies_cast['color'] = df_movies_cast['gender_filled'].map(gender_colors)


plt.figure(figsize=(20, 10))
plt.scatter(
    df_movies_cast['age_at_release'],
    df_movies_cast['budget'],
    c=df_movies_cast['color'],
    alpha=0.6,
    edgecolor='k'
)

plt.xlabel("Lead Actor/Actress Age at Release")
plt.ylabel("Movie Budget in million US dollars")
plt.title("Movie Budget vs Lead Actor/Actress Age by Gender")

#Set x-axis steps
plt.xticks(range(0, int(df_movies_cast['age_at_release'].max()) + 10, 10))


# Infobox
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Unknown', markerfacecolor='gray', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='Female', markerfacecolor='red', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='Male', markerfacecolor='blue', markersize=8),
    Line2D([0], [0], marker='o', color='w', label='Non-binary', markerfacecolor='green', markersize=8)
]
plt.legend(handles=legend_elements, title="Gender")

plt.show()


gender_labels = {0: "Unknown", 1: "Female", 2: "Male", 3: "Non-binary"}

df_movies_cast['gender_filled'].map(gender_labels).value_counts()

# streamlit_app.py
import streamlit as st
import pandas as pd

# Assuming df_movies_cast is already created
df_table = df_movies_cast[['budget', 'age_at_release', 'gender']].copy()

# Convert budget to millions for readability
df_table['budget'] = df_table['budget'] / 1_000_000
df_table.rename(columns={'budget': 'Budget (M USD)'}, inplace=True)

st.title("Movie Budget vs Lead Actor/Actress Age by Gender")

# Scatterplot with Streamlit's built-in chart
st.scatter_chart(
    df_table,
    x="age_at_release",
    y="Budget (M USD)",
    color="gender"
)

# Data table
st.subheader("Data Table")
st.dataframe(df_table)
