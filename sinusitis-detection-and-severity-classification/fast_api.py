from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
# from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import io

app = FastAPI()

# Set the correct model path on Google Drive
model_path = 'sinusities/inceptionv3_model_improved.h5'

# Load the model and labels
model = load_model(model_path, compile=False)
class_names = ["mild", "moderate", "severe"]
 

# Function to preprocess the image
def preprocess_image(file):
   try:
      # Open the image
      image = Image.open(file).convert("RGB")

      # Resize the image to (224, 224) as required by InceptionV3
      # Resize the image to (224, 224) as required by ResNet50
      # Resize the image to (224, 224) as required by VGG16
      size = (224, 224)
      image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
      image_array = np.asarray(image)

      # Normalize the image (same as the original InceptionV3 model preprocessing)
      normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

      # Create the array of the right shape for the model
      data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
      data[0] = normalized_image_array

      return data
   except Exception as e:
      raise ValueError(f"Error during image preprocessing: {e}")

# Function to predict the class of the image
def predict_image(data):
   try:
      # Make the prediction
      prediction = model.predict(data)
      index = np.argmax(prediction)
      class_name = class_names[index]
      confidence_score = prediction[0][index]

      return class_name, confidence_score
   except Exception as e:
      raise ValueError(f"Error during prediction: {e}")


# Define the API endpoint
@app.post("/predict")
async def predictAPI(file: UploadFile = File(...)):
   try:
      # Read the uploaded file as bytes
      file = await file.read()
      file_bytes = io.BytesIO(file)

      # Preprocess the image
      data = preprocess_image(file_bytes)

      # Predict the severity level
      class_name, confidence_score = predict_image(data)

      # Return the result as JSON
      return {
         "prediction": class_name.strip(),
         "confidence_score": float(confidence_score)  
      }
   except Exception as e:
      return {"error": str(e)}
    
 
