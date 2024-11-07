import IPython.display as display
import streamlit as st

st.markdown('''<h3 style='text-align: center; color: #023558;'>Extra information</h3>''', unsafe_allow_html=True)
st.markdown('''<p style='text-align: center; color: #000000;'></p>''', unsafe_allow_html=True)
st.markdown('''<h4 style='text-align: center; color: #2b8cbe;'>Markdown example</h4>''', unsafe_allow_html=True)
with open('example_data/test_md.md', 'r') as markdown_file:
    markdown_content = markdown_file.read()
st.markdown(markdown_content, unsafe_allow_html=True)
