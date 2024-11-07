import streamlit as st
st.set_page_config(layout="wide", page_title="MicW2Graph", page_icon="example_data/mona_logo.png")
st.logo("example_data/mona_logo.png")

st.markdown('''<h1 style='text-align: center; color: #023858;'>MicW2Graph</h1>''', unsafe_allow_html=True)

sections_pages = {}
homepage = st.Page('home/homepage.py', title='Homepage')
sections_pages['Home'] = [homepage]

Abundance_data = st.Page('Exploratory_Data_analysis/Exploratory_Data_analysis_Abundance_data.py', title='Abundance data')
Sample_data = st.Page('Exploratory_Data_analysis/Exploratory_Data_analysis_Sample_data.py', title='Sample data')
Extra_information = st.Page('Exploratory_Data_analysis/Exploratory_Data_analysis_Extra_information.py', title='Extra information')
sections_pages['Exploratory Data analysis'] = [Abundance_data, Sample_data, Extra_information]

Network_Visualization1 = st.Page('Microbial_Association_Networks/Microbial_Association_Networks_Network_Visualization1.py', title='Network Visualization1')
Network_Visualization2 = st.Page('Microbial_Association_Networks/Microbial_Association_Networks_Network_Visualization2.py', title='Network Visualization2')
Edge_list = st.Page('Microbial_Association_Networks/Microbial_Association_Networks_Edge_list.py', title='Edge list')
sections_pages['Microbial Association Networks'] = [Network_Visualization1, Network_Visualization2, Edge_list]

report_nav = st.navigation(sections_pages)
report_nav.run()