import json
import pandas as pd
import altair as alt
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Abundance data</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'></p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Top 5 species by biome (plotly)</h4>''', unsafe_allow_html=True)

with open('example_data/MicW2Graph/top_species_plot_biome.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
st.plotly_chart(plot_json, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Multiline plot (altair)</h4>''', unsafe_allow_html=True)

with open('example_data/altair_multilineplot.json', 'r') as plot_file:
    plot_json = json.load(plot_file)
altair_plot = alt.Chart.from_dict(plot_json)
st.vega_lite_chart(json.loads(altair_plot.to_json()), use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Abundance data for all studies (csv)</h4>''', unsafe_allow_html=True)
df = pd.read_csv('example_data/MicW2Graph/abundance_data_allbiomes.csv', delimiter=',')
st.dataframe(df, use_container_width=True)

st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Abundance data for all studies (excel)</h4>''', unsafe_allow_html=True)
df = pd.read_excel('example_data/MicW2Graph/abundance_data_allbiomes.xls')
st.dataframe(df, use_container_width=True)
