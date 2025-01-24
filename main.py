import streamlit as st
import pickle
import pandas as pd
st.title("MOVIE RECOMMENDATION SYSTEM!")
movie_list=pickle.load(open("movies2.pkl","rb"))
similarity=pickle.load(open("simi.pkl","rb"))
new_df=pd.DataFrame(movie_list)
st.write("Welcome to the Movie Recommendation System. We will recommend you some of the best movies based on your preferences. Let's get started!")
option=st.selectbox("How would you like to get recommendations?",new_df['title'].values)

def recommend(movie):
    movie_clean=movie.lower().replace(" ","")
    
    movie_title=pd.DataFrame(new_df['title'].str.replace(" ",""))
        
    movie_index=new_df[movie_title['title'].str.lower()==movie_clean].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x : x [1])[1:6]
    recomended_movies=[]
    for i in movie_list:
        recomended_movies.append(new_df.iloc[i[0]].title)
    return recomended_movies
        
if st.button("Recommend"):
    st.write("Movies similar to your choice are:")
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)