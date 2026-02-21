import pickle
import pandas as pd
import streamlit as st
import gzip

# Load the data

data = pickle.load(open('movie_dict.pkl',mode='rb'))
data = pd.DataFrame(data)
print(data)

# Load the similarity Score
with gzip.open('similarity.pkl.gz', mode='rb') as f:
    similarity = pickle.load(f)
    print(similarity)

# Final Function
def recommend(movie):

    recommended_movies = []

    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True, key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommended_movies.append(data.iloc[i[0]].title)

    return recommended_movies


# streamlit Web-App
st.title('Movies Recommendation System')

selected_movie = st.selectbox(
    "Select a movie to get recommendation",data['title'].values)

btn = st.button('Recommend')

if btn:
    list_of_movies = recommend(selected_movie)
    
    for movie in list_of_movies:
        st.write(movie)
