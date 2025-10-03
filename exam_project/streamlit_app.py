import streamlit as st
import pandas as pd
import altair as alt
import sys
import os
sys.path.append(os.path.abspath(".."))
from reader import generic_reader

df = generic_reader.read_csv_file_to_data_frame("movie_data/to_streamlit.csv")

# Multi-select for genders
gender_labels = ["Female", "Male", "Non-binary"]
genders = st.multiselect(
    "Choose genders",
    options=gender_labels,
    default=gender_labels
)

# Text input for searching actor/actress
actor_search = st.text_input("Search for an actor/actress by name:")

# Text input for searching actor/actress
movie_search = st.text_input("Search for a movie by name:")

# Filter dataframe by selected genders
filtered_df = df[df["gender_label"].isin(genders)]

# Further filter by actor/actress name if something is typed
if actor_search:
    filtered_df = filtered_df[filtered_df["name"].str.contains(actor_search, case=False, na=False)]

if movie_search:
    filtered_df = filtered_df[filtered_df["original_title"].str.contains(movie_search, case=False, na=False)]


# Show warning if nothing to display
if filtered_df.empty:
    st.warning("No data to display. Adjust gender selection or search term.")
else:
    chart = (
        alt.Chart(filtered_df)
        .mark_circle(size=60)
        .encode(
            x=alt.X('age_at_release:Q', title='Lead Actor/Actress Age at Release'),
            y=alt.Y('budget:Q', title='Movie Budget (USD)'),
            color=alt.Color(
                'gender_label:N',
                title="Gender",
                scale=alt.Scale(
                    domain=gender_labels,
                    range=['red', 'blue', 'green']
                )
            ),
            tooltip=[
                {'field': 'original_title', 'title': 'Movie Title'},
                {'field': 'name', 'title': 'Actor/Actress'},
                {'field': 'age_at_release', 'title': 'Age at Release'},
                {'field': 'gender_label', 'title': 'Gender'},
                {'field': 'vote_average', 'title': 'Rating'},
                {'field': 'budget', 'title': 'Budget (USD)'},
                {'field': 'revenue', 'title': 'Revenue (USD)'},
                {'field': 'release_date', 'title': 'Release Date'},
                              
            ]
        )
        .properties(
            title="Movie Budget vs Lead Actor/Actress Age by Gender",
            width=800,
            height=500
        )
    )
    st.altair_chart(chart, use_container_width=True)
