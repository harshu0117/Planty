import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import os

# Load the model
model_path = os.path.abspath("api/1.keras")
if not os.path.exists(model_path):
    st.error(f"Model not found at {model_path}")
    st.stop()

MODEL = tf.keras.models.load_model(model_path)
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# App Title
st.title("🥔 Potato Leaf Disease Detection")
st.write("Upload an image of a potato leaf, and the model will predict whether it's healthy or has a disease.")

# 📝 Instructions
st.markdown("""
### 🌱 How to Use:
1. **Upload a clear image** of a potato leaf.
2. The model detects **Early Blight** and **Late Blight** diseases.
3. **For best results:**  
   - Use a **real photo of a potato leaf** from your field.  
   - Or **download** a sample image of a potato leaf with Early/Late Blight and test it here.  
4. The model was trained on **potato leaves only**, so predictions for other plants may not be accurate.

### 🍃 Disease Information:
- **Early Blight**: Brown spots with concentric rings on older leaves.
- **Late Blight**: Dark, water-soaked lesions with white mold on leaf edges.

""")

# File Uploader
uploaded_file = st.file_uploader("📸 Upload a Potato Leaf Image", type=["jpg", "jpeg", "png"])

def read_file_as_image(data) -> np.ndarray:
    """Converts uploaded image to NumPy array"""
    image = np.array(Image.open(io.BytesIO(data)).convert("RGB"))
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼 Uploaded Image", use_container_width=True)

    # Convert image to NumPy array
    image_array = read_file_as_image(uploaded_file.getvalue())
    img_batch = np.expand_dims(image_array, 0)

    # Make prediction
    with st.spinner("🔍 Analyzing..."):
        predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    st.success(f"🩺 **Prediction:** {predicted_class}")
    st.write(f"📊 **Confidence:** {confidence * 100:.2f}%")
