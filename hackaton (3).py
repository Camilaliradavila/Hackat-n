import streamlit as st
import pandas as pd
 
st.write("""
# AIRA 
Your AI-based Research Assistant
""")

uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)