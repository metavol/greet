import streamlit as st
import numpy as np

name = st.text_input("your name")
if st.button("click me"):
    st.text("Hello, " + name)

a = np.arange(10)
b = a.sum()
st.write(b)
