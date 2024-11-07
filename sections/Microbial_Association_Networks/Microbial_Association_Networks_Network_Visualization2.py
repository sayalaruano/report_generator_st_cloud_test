import json
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Network Visualization2</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'></p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Network2 (edge list csv)</h4>''', unsafe_allow_html=True)

with open('example_data/network2.html', 'r') as f:
    html_data = f.read()

st.markdown(f"<p style='text-align: center; color: black;'> <b>Number of nodes:</b> 9 </p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: black;'> <b>Number of relationships:</b> 14 </p>", unsafe_allow_html=True)

# Streamlit checkbox for controlling the layout
control_layout = st.checkbox('Add panel to control layout', value=True)
net_html_height = 1200 if control_layout else 630

# Load HTML into HTML component for display on Streamlit
st.components.v1.html(html_data, height=net_html_height)