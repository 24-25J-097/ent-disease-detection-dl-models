# Eardrum Endoscopy Classification API

This repository contains an API built using **FastAPI** to classify endoscopy images as valid or invalid cholesteatoma. The application is designed for quick deployment and easy accessibility, using **Ngrok** for external testing.

---

## Features

- **Deep Learning-Powered**: Uses a pre-trained model to classify images.
- **FastAPI Framework**: High-performance API for seamless integration.
- **Ngrok Integration**: Exposes the API to be accessed from mobile or external devices.

---

## Requirements

- **Python 3.10.2**
- **Required Libraries**: 
  - `FastAPI`
  - `Uvicorn`
  - `TensorFlow`
  - `NumPy`
  - `Python Pillow (Imaging Library)`
  - `OpenCV`
  - `Python-Multipart`
- **Ngrok** (Download from [ngrok.com/download](https://ngrok.com/download)).

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

To start the Cholesteatoma FastAPI server, use the following command:
```bash
uvicorn ch_server:app --reload --port 4000

# OR Use FastApi command

fastapi dev ch_server.py
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
### Health Check
To verify the API is running, send a GET request:
```bash
curl http://127.0.0.1:4000/
# Or use the public Ngrok URL:
curl https://monarch-witty-platypus.ngrok-free.app/
```
