import streamlit as st
import pandas as pd
import altair as alt
import sys
import os
sys.path.append(os.path.abspath(".."))
from reader import generic_reader

@st.cache_data
def load_data():
    return generic_reader.read_csv_file_to_data_frame("movie_data/to_streamlit.csv")

df = load_data()

min_age = int(df['age_at_release'].min())
max_age = int(df['age_at_release'].max())

if "age_range" not in st.session_state:
    st.session_state.age_range = (min_age, max_age)
if "actor_search" not in st.session_state:
    st.session_state.actor_search = ""
if "movie_search" not in st.session_state:
    st.session_state.movie_search = ""

def reset_age_slider():
    st.session_state.age_range = (min_age, max_age)

def clear_actor_search():
    st.session_state.actor_search = ""

def clear_movie_search():
    st.session_state.movie_search = ""


st.header("Placeholder title")

#Multiselect for genders
gender_labels = ["Female", "Male", "Non-binary"]
genders = st.multiselect(
    "Choose genders",
    options=gender_labels,
    default=gender_labels
)

#Textfield for actor search and clear button
st.text_input("Search for an actor/actress by name:", key="actor_search")
st.button("Clear", on_click=clear_actor_search, key="clear_actor")

#Textfield for movie search and clear button
st.text_input("Search for a movie by title:", key="movie_search")
st.button("Clear", on_click=clear_movie_search, key="clear_movie")

#Slider for age limtes and reset button
st.slider(
    "Select age range for actors/actresses:",
    min_value=min_age,
    max_value=max_age,
    value=st.session_state.age_range,
    key="age_range"
)
st.button("Reset", on_click=reset_age_slider, key="reset_age")

#Filters
filtered_df = df[df["gender_label"].isin(genders)]

if st.session_state.actor_search:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(st.session_state.actor_search, case=False, na=False)
    ]

if st.session_state.movie_search:
    filtered_df = filtered_df[
        filtered_df["original_title"].str.contains(st.session_state.movie_search, case=False, na=False)
    ]

filtered_df = filtered_df[
    (filtered_df['age_at_release'] >= st.session_state.age_range[0]) &
    (filtered_df['age_at_release'] <= st.session_state.age_range[1])
]


if filtered_df.empty:
    st.warning("No data to display. Adjust filters or search terms.")
else:

    gender_counts = filtered_df['gender_label'].value_counts()

    st.markdown("### Number of movies/actors displayed by gender:")
    for gender in gender_labels:
        count = gender_counts.get(gender, 0)
        st.write(f"{gender}: {count}")


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
                {'field': 'budget_2023_usd', 'title': 'Budget (USD)'},
                {'field': 'revenue_2023_usd', 'title': 'Revenue (USD)'}
            ]
        )
        .properties(
            title="Movie Budget vs Lead Actor/Actress Age by Gender",
            width=800,
            height=500
        )
    )

    st.altair_chart(chart, use_container_width=True)