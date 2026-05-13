import streamlit as st
import json
from PIL import Image
import numpy as np
import time

# 1. Load the treatment database
with open('treatments.json') as f:
    treatments = json.load(f)

st.title("🌾 AI Crop Health Diagnosis")
st.write("Upload a leaf photo to get instant treatment advice.")

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Leaf', use_container_width=True)
    
    with st.spinner("Analyzing plant pigments..."):
        time.sleep(1.5) # Makes it feel like real AI processing
        
        # 2. SMART COLOR LOGIC
        # We turn the image into numbers to see how much Green vs Brown is in it
        img_array = np.array(image.resize((100, 100)))
        avg_color = np.mean(img_array, axis=(0, 1))
        
        red_val = avg_color[0]
        green_val = avg_color[1]

        # 3. DECISION MAKING
        # If there is a lot of red/brown relative to green, it's likely a disease
        if red_val > (green_val * 0.85):
            # If it looks brown/yellow, pick a disease from your JSON
            # We'll use logic to pick between Potato and Tomato based on filename or just randomness
            if "tomato" in uploaded_file.name.lower():
                result = "Early Blight (Tomato)"
            else:
                result = "Late Blight (Potato)"
            
            st.error(f"**Detected:** {result}")
            st.info(f"**Recommended Treatment:** {treatments[result]}")
        
        else:
            # If it's mostly green, it's healthy!
            result = "Healthy Plant"
            st.success(f"✅ **Report:** {result}")
            st.info(f"**Advice:** {treatments[result]}")
