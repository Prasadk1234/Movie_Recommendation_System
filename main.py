import streamlit as st
import pickle
import pandas as pd



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.set_page_config(
    page_title="Welcome",
    page_icon="🎬",
)
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.write("# MOVIE RECOMMENDATION SYSTEM 🎥 🎬")

selected_movie_name = st.selectbox('Search for movie', movies['title'].values)

if st.button('Recommand'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
