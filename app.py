import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
df = pd.read_csv("clean.csv")

# Load trained TF-IDF vectorizer
with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Create TF-IDF matrix for movies
tfidf_matrix = tfidf.transform(df["Storyline"])


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

        # Get Top 5 recommendations
        top_indices = similarity_scores.argsort()[-5:][::-1]

        st.subheader("Top 5 Recommended Movies")

        for rank, i in enumerate(top_indices, start=1):
            st.write(f"### {rank}. 🎥 {df.iloc[i]['Movie Name']}")

            st.write(df.iloc[i]["Storyline"])

            st.write(
            "Similarity Score:",
            round(similarity_scores[i], 3)
    )

            st.write("---")

    else:
        st.warning("Please enter a storyline.")