import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly.express as px
#import warnings

#from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.decomposition import PCA

st.set_page_config(page_title="Streamlit Data App", layout="wide")

warnings.filterwarnings("ignore")

sns.set_context("talk")


st.title("Movies Analysis")

df = pd.read_csv("movies.csv")

st.write(df)