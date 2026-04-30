import streamlit as st
import google.generativeai as genai
import json

# Securely load the API key from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Use the 1.5 Flash model
model = genai.GenerativeModel('gemini-1.5-flash') 

# ... the rest of your LeafGuard-AI UI code ...
