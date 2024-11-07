import json
import plotly.io as pio
import pandas as pd
import dataframe_image as dfi
import streamlit as st
from itables import show

st.markdown('''<h3 style='text-align: center; color: #023558;'>Sample data</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'></p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Number of samples per study (png)</h4>''', unsafe_allow_html=True)

st.image('example_data/MicW2Graph/number_samples_per_study.png', caption='', use_column_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Sampling countries for all studies (plotly)</h4>''', unsafe_allow_html=True)

with open('example_data/MicW2Graph/pie_plot_countries.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Sample data for all studies (txt)</h4>''', unsafe_allow_html=True)
df = pd.read_csv('example_data/MicW2Graph/sample_info_allbiomes.txt', sep='\t')
st.dataframe(df, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Sample data for all studies (parquet)</h4>''', unsafe_allow_html=True)
df = pd.read_parquet('example_data/MicW2Graph/sample_info_allbiomes.parquet')
st.dataframe(df, use_container_width=True)
