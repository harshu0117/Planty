import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import os

# Load the model
model_path = os.path.abspath("api/1.keras")
# st.write(f"Loading model from: {model_path}")
if not os.path.exists(model_path):
    st.error(f"Model not found at {model_path}")
    st.stop()

MODEL = tf.keras.models.load_model(model_path)
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

st.title("🌿 Plant Disease Detection")
st.write("Upload an image of a plant leaf, and the model will predict the disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(io.BytesIO(data)).convert("RGB"))
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Convert image to NumPy array
    image_array = read_file_as_image(uploaded_file.getvalue())
    img_batch = np.expand_dims(image_array, 0)
    
    # Make prediction
    with st.spinner("Predicting..."):
        predictions = MODEL.predict(img_batch)
    
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    
    st.success(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence * 100:.2f}%")
