import streamlit as st
import pandas as pd
import altair as alt


df_movies_cast = pd.read_csv("movie_data/to_streamlit.csv")

gender_labels = {
    0: 'Unknown',
    1: 'Female',
    2: 'Male',
    3: 'Non-binary'
}

# Make sure gender is numeric
df_movies_cast['gender'] = pd.to_numeric(df_movies_cast['gender'], errors='coerce').fillna(0).astype(int)
df_movies_cast['gender_label'] = df_movies_cast['gender'].map(gender_labels)



st.write("Test")

chart = (
    alt.Chart(df_movies_cast)
    .mark_circle(size=60)
    .encode(
        x=alt.X('age_at_release:Q', title='Lead Actor/Actress Age at Release'),
        y=alt.Y('budget:Q', title='Movie Budget (USD)'),
        color=alt.Color(
            'gender_label:N',
            title="Gender",
            scale=alt.Scale(
                domain=['Unknown', 'Female', 'Male', 'Non-binary'],
                range=['gray', 'red', 'blue', 'green']
            )
        ),
        tooltip=['original_title', 'age_at_release', 'budget', 'gender_label']
    )
    .properties(
        title="Movie Budget vs Lead Actor/Actress Age by Gender",
        width=800,
        height=500
    )
)

st.altair_chart(chart, use_container_width=True)
