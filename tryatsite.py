import streamlit as st
from pfication import pfication

st.title("П-потеха")
st.write("Привет! Этот сайт призван помочь тебе в том, чтобы придумать определение для слова для игры в 'П'.")
game_word = "кабачок"
if st.button('Поясните, пожалуйста!'):
    st.write(*pfication(st.text_input("Пожалуйста, предоставьте понятие для пояснения", "", placeholder='например, кабачок')))
st.write(*pfication(gameword))
