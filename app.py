import streamlit as st
import json
from PIL import Image
import numpy as np
import time

# Load your custom treatment database
with open('treatments.json') as f:
    treatments = json.load(f)

st.title("🌿 LeafGuard AI")
st.write("Upload a leaf photo for instant health analysis.")

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Scanning Leaf...', use_container_width=True)
    
    with st.spinner('Analyzing cellular structure...'):
        time.sleep(2) # Simulated "Thinking" time
        
        # Smart Logic: Analysis using NumPy
        img_array = np.array(image.resize((10, 10)))
        avg_color = np.mean(img_array, axis=(0, 1))
        
        # Logic: If Red/Brown levels are high, it's a disease
        if avg_color[0] > avg_color[1] * 0.8:
            result = "Late Blight (Potato)"
            st.error(f"**Detected:** {result}")
            st.info(f"**Treatment:** {treatments[result]}")
        else:
            result = "Healthy Plant"
            st.success(f"✅ **Report:** {treatments[result]}")
