# https://discuss.streamlit.io/t/colored-boxes-around-sections-of-a-sentence/3201/2

import streamlit as st

def local_css(style.css):
    with open(style.css) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
