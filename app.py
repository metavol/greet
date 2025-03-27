import streamlit as st

name = st.text_input("your name")
if st.button("click me"):
    st.text("Hello, " + name)
