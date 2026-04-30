import streamlit as st
from google import genai
import json

# Streamlit securely loads the API key from its secrets manager
api_key = st.secrets["GEMINI_API_KEY"]

# Initialize the new GenAI client
client = genai.Client(api_key=api_key)

# ... your LeafGuard-AI UI code goes here ...

# Note: When you actually generate a response later in your code, 
# the new syntax for the 3.0 model looks like this:
#
# response = client.models.generate_content(
#     model='gemini-3.0-flash',
#     contents='Your prompt or leaf image data here'
# )
