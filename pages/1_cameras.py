import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_extras.dataframe_explorer import dataframe_explorer

df = pd.read_csv('datasets/camera.csv')

filtered_df = dataframe_explorer(df, case=True)

st.dataframe(filtered_df,use_container_width=True)
