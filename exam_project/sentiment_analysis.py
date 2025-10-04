import streamlit as st
import pandas as pd
from transformers import pipeline
import altair as alt
import sys
import os
sys.path.append(os.path.abspath(".."))
from reader import generic_reader


@st.cache_data
def load_data():
    return generic_reader.read_csv_file_to_data_frame("movie_data/to_streamlit.csv")
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")


# Use cached function
df = load_data()
classifier = load_model()


st.title("Movie Overview Sentiment Analyzer")


def clear_movie_search():
    st.session_state.movie_search = ""
    
st.text_input("Search for a movie by title:", key="movie_search")
st.button("Clear", on_click=clear_movie_search, key="clear_movie")


search_term = st.session_state.movie_search.strip()

if search_term:
    results = df[df['original_title'].str.contains(search_term, case=False, na=False)]

    if len(results) > 0:
        st.subheader(f"Results for '{search_term}':")

        for _, row in results.iterrows():
            st.markdown(f"### 🎞️ {row['original_title']}")
            st.write(row['overview'])

            # Perform sentiment analysis
            with st.spinner("Analyzing sentiment..."):
                result = classifier(row['overview'])[0]
                label = result['label']
                score = result['score']

                st.write(f"**Sentiment:** {label} ({score:.2f})")

                # Optional: visualize with Altair
                chart_data = pd.DataFrame({
                    'Sentiment': [label, 'Opposite'],
                    'Score': [score, 1 - score]
                })
                chart = alt.Chart(chart_data).mark_bar().encode(
                    x='Sentiment',
                    y='Score',
                    color='Sentiment'
                ).properties(width=300, height=200)
                st.altair_chart(chart, use_container_width=True)

    else:
        st.warning("No movies found with that title.")
else:
    st.info("Enter a movie title above to get started.")