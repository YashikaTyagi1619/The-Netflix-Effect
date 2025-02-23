# streamlit run app.py  24 and 45 ..... above 45

import streamlit as st
import streamlit.components.v1 as components
import pickle
import requests
import json

def fetch_poster(m_name):
    url =  f"http://www.omdbapi.com/?t={m_name}&apikey=b01bae5f"
    data = requests.get(url)
    data = data.json()
    poster_path = data['Poster']
    #full_path = poster_path
    return poster_path


movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")

# imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [

    fetch_poster('Avengers: Infinity War'),
    fetch_poster('Hellraiser: Deader'),
    fetch_poster("My Boss's Daughter"),
    fetch_poster('Capone'),
    fetch_poster('Bewitched'),
    fetch_poster('The Women'),
    fetch_poster('The Godfather: Part II'),
    fetch_poster('The Dark Knight'),
    fetch_poster('City of God'),
    fetch_poster('The Great Dictator'),
    fetch_poster('Hope'),
    fetch_poster('Project X')

    ]
for poster in imageUrls:
    st.image(poster)

# imageCarouselComponent(imageUrls=imageUrls, height=200)

select_value = st.selectbox("Selct movies from dropdown",movies_list)



def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        #movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies.iloc[i[0]].title))
        #m_name1 = str(movies.iloc[i[0]].title)
        #m_name2 = m_name1.strip().replace(' ',"+")

        #recommend_poster.append(fetch_poster(movies_id,m_name=m_name2))
    return recommend_movie,recommend_poster

if st.button("Show Recommand"):
    # global movie_name
    movie_name ,movie_poster = recommend(select_value)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])