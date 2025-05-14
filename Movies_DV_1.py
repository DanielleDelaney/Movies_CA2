import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Streamlit Data App", layout="wide")


st.title("Movies Analysis")

df = pd.read_csv("movies.csv")

st.write(df)