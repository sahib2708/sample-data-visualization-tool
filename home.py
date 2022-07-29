import streamlit as st
from PIL import Image

def home():
    
    
    st.title('LAS tool sample 1')
    st.write('## Welcome to the LAS tool sample')
    st.write('### Under progress, developed by **Girija Rathore** & **Sahib Singh Kapoor**')
    st.write('''LAS tool is a tool designed using Python and Streamlit to help visualize,showcase LAS files with certain features.''')
    st.write('To begin using the app, load your LAS file using the upload option on the sidebar. Then navigate to the relevant features using the Navigation menu.')
    st.write('\n')
    st.write('## Available Features on tool')
    st.write('**Header Info:** Information from the LAS file header.')
    st.write('**Data Information:** Information about the curves contained within the LAS file, including names, statisics and raw data values.')
    st.write('**Data Visualisation:** Visualisation tools to view las file data on a log plot, crossplot and histogram.')
