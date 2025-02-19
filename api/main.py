from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os

# Define the correct model path
model_path = os.path.abspath("api/1.keras")
print("Loading model from:", model_path)  # Debugging

# Check if model exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at {model_path}")

# Load the model (Keras V3 format)
MODEL = tf.keras.models.load_model(model_path)

# Define class names
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

app = FastAPI()


# Update CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    """Convert uploaded file to a NumPy array"""
    image = np.array(Image.open(BytesIO(data)).convert("RGB"))  # Ensure RGB format
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Predict plant disease from uploaded image"""
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)

    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])

    return {"class": predicted_class, "confidence": float(confidence)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

