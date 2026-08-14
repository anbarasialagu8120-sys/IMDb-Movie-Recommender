# 🎬 IMDb Movie Recommendation System Using Storylines

## 📌 Project Overview

The **IMDb Movie Recommendation System Using Storylines** is a content-based movie recommendation system that recommends movies based on the similarity between movie storylines.

The project uses **Natural Language Processing (NLP)** techniques to process movie storylines and **TF-IDF (Term Frequency-Inverse Document Frequency)** to convert text into numerical vectors.

Then, **Cosine Similarity** is used to measure the similarity between the user's input storyline and the movie storylines.

The application is developed using **Streamlit**, where users can enter a movie storyline and receive the **Top 5 similar movie recommendations**.

---

## 🎯 Problem Statement

Finding a suitable movie based on a user's preferred story or plot can be difficult when there are thousands of movies available.

This project solves this problem by developing a recommendation system that accepts a movie storyline as input and recommends the most similar movies based on storyline similarity.

---

## 💡 Business Use Cases

### 1. Movie Recommendation
Users can enter a movie storyline and receive the Top 5 movies with similar storylines.

### 2. Entertainment Suggestions
The system helps users discover movies based on their story preferences.

### 3. Content-Based Recommendation
Movies are recommended based on the content of their storylines rather than user ratings or popularity.

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Selenium

### NLP Techniques
- Text Cleaning
- Lowercase Conversion
- Punctuation Removal
- Lemmatization
- Stopword Removal
- TF-IDF Vectorization

### Recommendation Technique
- Cosine Similarity

### Data Visualization
- Matplotlib
- Streamlit

---

## 📂 Dataset

The dataset contains IMDb movie information for movies released in 2024.

### Columns

| Column | Description |
|---|---|
| Movie Name | Name of the movie |
| Storyline | Movie plot/storyline |

The movie data was collected from IMDb using Selenium and stored in CSV format.

---

## 🔄 Project Workflow

```text
IMDb Movie Data
       ↓
Data Scraping using Selenium
       ↓
Data Cleaning
       ↓
Text Preprocessing
       ↓
EDA
       ↓
TF-IDF Vectorization
       ↓
Cosine Similarity
       ↓
Top 5 Movie Recommendations
       ↓
Streamlit Application
