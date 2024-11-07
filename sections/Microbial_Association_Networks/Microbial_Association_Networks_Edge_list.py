import dataframe_image as dfi
import pandas as pd
import streamlit as st
from itables import show

st.markdown('''<h3 style='text-align: center; color: #023558;'>Edge list</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'></p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Edge list (csv)</h4>''', unsafe_allow_html=True)
df = pd.read_csv('example_data/MicW2Graph/man_example.csv', delimiter=',')
st.dataframe(df, use_container_width=True)
