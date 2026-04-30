import streamlit as st
import google.generativeai as genai
import json # for your treatments.json

# Streamlit securely loads the API key from its secrets manager
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Update the model name to the latest 1.5 version to fix the limit issue
model = genai.GenerativeModel('gemini-1.5-flash') 

# ... the rest of your LeafGuard-AI code remains the same ...
