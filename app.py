import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import os
import gdown

# 1. Download and Load the real AI brain from Google Drive
@st.cache_resource
def load_my_model():
    # Replace the ID below with the ID from your Google Drive link
    file_id = 'YOUR_GOOGLE_DRIVE_FILE_ID_HERE'
    url = f'https://drive.google.com/uc?id={file_id}'
    output = 'leafguard_model.h5'
    
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)
    
    return tf.keras.models.load_model(output)

model = load_my_model()

# 2. Define the classes (PlantVillage dataset)
CLASS_NAMES = ['Apple_scab', 'Apple_black_rot', 'Apple_cedar_rust', 'Apple_healthy', 'Blueberry_healthy', 'Cherry_powdery_mildew', 'Cherry_healthy', 'Corn_gray_leaf_spot', 'Corn_common_rust', 'Corn_northern_leaf_blight', 'Corn_healthy', 'Grape_black_rot', 'Grape_black_measles', 'Grape_leaf_blight', 'Grape_healthy', 'Orange_haunglongbing', 'Peach_bacterial_spot', 'Peach_healthy', 'Bell_pepper_bacterial_spot', 'Bell_pepper_healthy', 'Potato_early_blight', 'Potato_late_blight', 'Potato_healthy', 'Raspberry_healthy', 'Soybean_healthy', 'Squash_powdery_mildew', 'Strawberry_leaf_scorch', 'Strawberry_healthy', 'Tomato_bacterial_spot', 'Tomato_early_blight', 'Tomato_late_blight', 'Tomato_leaf_mold', 'Tomato_septoria_leaf_spot', 'Tomato_spider_mites', 'Tomato_target_spot', 'Tomato_yellow_leaf_curl', 'Tomato_mosaic_virus', 'Tomato_healthy']

with open('treatments.json', 'r') as f:
    treatments = json.load(f)

st.title("🌿 LeafGuard AI")
st.write("Upload a leaf photo for instant diagnosis.")

uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    img = image.resize((128, 128))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) / 255.0

    predictions = model.predict(img_array)
    result_index = np.argmax(predictions[0])
    outcome = CLASS_NAMES[result_index]
    
    st.subheader(f"Diagnosis: {outcome.replace('_', ' ')}")
    
    simple_key = "Potato_late_blight" if "Potato" in outcome else "Tomato_late_blight"
    st.info(f"**Recommended Action:** {treatments.get(simple_key, 'Consult a local expert for specific chemical ratios.')}")
