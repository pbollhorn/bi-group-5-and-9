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

#Test of caching data
@st.cache_data
def analyze_sentiment(text):
    return classifier(text)[0]
    
    
st.text_input("Search for a movie by title:", key="movie_search")
st.button("Clear", on_click=clear_movie_search, key="clear_movie")

search_term = st.session_state.movie_search.strip()


def select_movie(title):
    st.session_state.movie_search = title

if search_term:
    results = df[df['original_title'].str.contains(search_term, case=False, na=False)]

    if len(results) > 0:
        st.markdown("### Search Result Titles (click to select)")
        cols = st.columns(min(len(results), 5)) 
        for i, (_, row) in enumerate(results.iterrows()):
            with cols[i % 5]:
                st.button(
                    row['original_title'],
                    key=f"card_{i}",
                    on_click=lambda title=row['original_title']: st.session_state.update({"movie_search": title})
                )

        # --- Full results list below ---
        st.subheader(f"Results for '{search_term}':")
        for _, row in results.iterrows():
            st.markdown(f"**{row['original_title']}**")
            st.write(row['overview'])

            with st.spinner("Analyzing sentiment..."):
                result = analyze_sentiment(row['overview'])
                label = result['label']
                score = result['score']

            st.write(f"**Sentiment:** {label} ({score:.2f})")

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