# Medical Image Analysis API

This repository contains an API built using **FastAPI** for medical image analysis. It includes deep learning models.

The application is designed for easy deployment and can be accessed externally using **Ngrok** for testing from mobile or other devices.

## Folder Structure

- cholesteatoma_detection_and_classification
   - accuracy-comparison
   - cholesteatoma
- foreign-objects
   - lateral-classifier
   - yolo-nas
- pharyngitis
   - pharyngitis_balanced (Dataset)
- sinusitis_detection_and_severity_classification
   - accuracy-comparison
   - sinusitis
   - waters_view_validator

## Features

- **Deep Learning-Powered**: Uses a pre-trained model to classify images.
- **FastAPI Framework**: High-performance API for seamless integration.
- **Ngrok Integration**: Exposes the API to be accessed from mobile or 

 
## Requirements

- **Python 3.10.2**
- **Required Libraries**: 
  - `FastAPI`
  - `Uvicorn`
  - `TensorFlow`
  - `NumPy` (for numerical operations)
  - `Python Pillow (Imaging Library)` (for image processing)
  - `OpenCV` (for image preprocessing)
  - `Python-Multipart` (for handling file uploads)
- **Ngrok** (Download from [ngrok.com/download](https://ngrok.com/download)).


## To install the required dependencies, run:

```bash
pip install -r requirements.txt
```
#### OR
Install Python dependencies:
```bash
pip install tensorflow==2.10.0
pip install numpy==1.23.0
pip install fastapi
pip install uvicorn
pip install pillow
pip install opencv-python
pip install python-multipart
```
### Steps to Run the Application
#### Run the FastAPI Application.

To start the FastAPI server, use the following command:
```bash
uvicorn server:app --reload --port 4000

# OR Use FastApi command

fastapi dev server.py
```
This will start the application locally at http://127.0.0.1:4000/.

#### Expose the API for Mobile Access
To make the API accessible from external devices (e.g., mobile apps), run Ngrok:
```bash
ngrok http --domain=monarch-witty-platypus.ngrok-free.app 4000
```
Get the domain name from the ngrok dashboard

**This will expose the application at the URL:**
```bash
https://monarch-witty-platypus.ngrok-free.app
```
You can now use this public URL in your mobile app or for external testing.

## Testing the API
### API Document  
Test route in FastAPI Swagger UI.
```
curl http://127.0.0.1:4000/docs
```
### END POINTS 
Test route to check if the API server is running.
```
curl http://127.0.0.1:4000/api/test
```
Endpoint to upload a file for sinusitis detection and severity classification.
   - File: The Water's View XRay image file for sinusitis detection.
```
curl http://127.0.0.1:4000/api/sinusitis/analyze
```
Endpoint to upload a file for cholesteatoma detection and stages classification.
   - File: Middle Ear Endoscopy image file for cholesteatoma detection.
```
curl http://127.0.0.1:4000/api/cholesteatoma/analyze
```
Endpoint to upload a file for pharyngitis detection and severity classification.

   - File: The image file for pharyngitis detection.
```
curl http://127.0.0.1:4000/api/pharyngitis/analyze
```

### Health Check
To verify the API is running, send a GET request:
```bash
curl http://127.0.0.1:4000/

# Or use the public Ngrok URL:
curl https://monarch-witty-platypus.ngrok-free.app/
```
