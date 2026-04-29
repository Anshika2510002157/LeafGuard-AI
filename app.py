import streamlit as st
import json
from PIL import Image

# Load your custom treatment database
with open('treatments.json') as f:
    treatments = json.load(f)

st.title("🌾 AI Crop Health Diagnosis")
st.write("Upload a leaf photo taken in daylight to get instant treatment advice.")

# The upload button for the farmer
uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png"])

if uploaded_file is not None:
    # Show the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Leaf', use_column_width=True)
    
    st.write("🔍 Analyzing plant health...")
    
    # NOTE: We will plug the actual AI Model in here later!
    # For now, we simulate a result to test the website.
    simulated_disease = "Late Blight (Potato)" 
    
    st.error(f"**Detected:** {simulated_disease}")
    st.info(f"**Recommended Treatment:** {treatments[simulated_disease]}")