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

df = load_data()


st.title("Movie Overview Analyzer")


analysis_mode = st.radio(
    "Choose analysis type:",
    ["Sentiment Analysis", "Emotion Classification"]
)

# --- Load appropriate model ---
@st.cache_resource
def load_model(mode):
    if mode == "Sentiment Analysis":
        return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    else:
        return pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            return_all_scores=True
        )

analyzer = load_model(analysis_mode)

# --- Text input and clear ---
def clear_movie_search():
    st.session_state.movie_search = ""

st.text_input("Search for a movie by title:", key="movie_search")
st.button("Clear", on_click=clear_movie_search, key="clear_movie")

search_term = st.session_state.movie_search.strip()


# --- Select movie callback ---
def select_movie(title):
    st.session_state.movie_search = title


# --- Main search logic ---
if search_term:
    results = df[df['original_title'].str.contains(search_term, case=False, na=False)]

    if len(results) > 0:
        st.markdown("### Search Result Titles")
        cols = st.columns(min(len(results), 5))
        for i, (_, row) in enumerate(results.iterrows()):
            with cols[i % 5]:
                st.button(
                    row['original_title'],
                    key=f"card_{i}",
                    on_click=lambda title=row['original_title']: select_movie(title)
                )

        # --- Full results list below ---
        st.subheader(f"Results for '{search_term}':")
        for _, row in results.iterrows():
            st.markdown(f"**{row['original_title']}**")
            st.write(row['overview'])

            with st.spinner(f"Analyzing {analysis_mode.lower()}..."):
                result = analyzer(row['overview'])

            # --- Display ---
            if analysis_mode == "Sentiment Analysis":
                label = result[0]['label']
                score = result[0]['score']
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

            else:  # Emotion Classification
                df_emotions = pd.DataFrame(result[0])
                st.write("**Top emotions:**")
                chart = alt.Chart(df_emotions).mark_bar().encode(
                    x=alt.X('label', sort='-y'),
                    y='score',
                    color='label'
                ).properties(width=400, height=200)
                st.altair_chart(chart, use_container_width=True)

    else:
        st.warning("No movies found with that title.")
else:
    st.info("Enter a movie title above to get started.")