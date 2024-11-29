from fastapi import FastAPI, File, UploadFile
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model
import numpy as np
import io

app = FastAPI()

# File paths
model_path = 'pharyngitis_model_mobilenetv2.h5'

# Define the API endpoint
@app.post("/pharyngitis")
async def predictAPI(file: UploadFile = File(...)):
   try:
      file = await file.read()
      file_bytes = io.BytesIO(file)

      # Load the model
      model = load_model(model_path, compile=False)

      # Define the class names
      class_names = ["Normal", "Moderate", "Tonsillitis"]

      # Prepare input image
      data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
      image = Image.open(file_bytes).convert("RGB")
      image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
      image_array = np.asarray(image)
      normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
      data[0] = normalized_image_array

      # Predict
      prediction = model.predict(data)
      index = np.argmax(prediction)
      class_name = class_names[index]
      confidence_score = prediction[0][index]

      return {
         "prediction": class_name.strip(),
         "confidence_score": float(confidence_score)  
      }
   except Exception as e:
      return {"error": str(e)}