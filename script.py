import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# My first app

Hello *World!*

"""
)

st.title("this is a title")

st.header("This is a header")

st.write("this is  a regular text")

dictionary_sample = {
    "key":1,
    "name": "Thomas"
}

st.write(dictionary_sample)

st.sidebar.write("Sidebar goes here:")

df = pd.DataFrame(np.random.randn(50,20), columns = ('col %d' % i for i in range(20)))

st.dataframe(df)