import streamlit as st
import pickle
import pandas as pd
import requests
md_list=pickle.load(open('md.pkl','rb'))
s_list=pickle.load(open('s.pkl','rb'))
movie=pd.DataFrame(md_list)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(option):
    movie_index=movie[movie['title']==option].index[0]
    dist=s_list[movie_index]
    movie_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[0:6]
    rec=[]
    id=[]
    for i in movie_list:
        id.append(fetch_poster(movie.iloc[i[0]].movie_id))
        rec.append(movie.iloc[i[0]].title)
    return rec,id
        


st.title("Movie Recomendation")
option = st.selectbox(
   "Enter movie",
   movie['title'].values,
   index=None,
   placeholder="Select movie",
)
if st.button('Recommend'):
    rec,id=recommend(option)
    col1, col2, col3, col4, col5,col6 = st.columns(6)
    with col1:
        st.text(rec[0])
        st.image(id[0])
    with col2:
        st.text(rec[1])
        st.image(id[1])

    with col3:
        st.text(rec[2])
        st.image(id[2])
    with col4:
        st.text(rec[3])
        st.image(id[3])
    with col5:
        st.text(rec[4])
        st.image(id[4])
    with col6:
        st.text(rec[5])
        st.image(id[5])