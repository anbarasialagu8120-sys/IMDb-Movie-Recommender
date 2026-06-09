import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
df = pd.read_csv("clean_movie.csv")   # unga CSV file name

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Storyline'])

# Streamlit UI
st.title("🎬 IMDb Movie Recommendation System")
st.write("Enter a movie storyline and get Top 5 similar movies")

user_storyline = st.text_area("Enter Storyline")

if st.button("Recommend Movies"):

    if user_storyline.strip() != "":

        # Convert user input into TF-IDF vector
        user_vector = tfidf.transform([user_storyline])

        # Calculate similarity
        similarity_scores = cosine_similarity(
            user_vector,
            tfidf_matrix
        ).flatten()

        # Top 5 recommendations
        top_indices = similarity_scores.argsort()[-5:][::-1]

        st.subheader("Top 5 Recommended Movies")

        for i in top_indices:
            st.write("### 🎥", df.iloc[i]["Movie Name"])
            st.write(df.iloc[i]["Storyline"])
            st.write("---")

    else:
        st.warning("Please enter a storyline.")