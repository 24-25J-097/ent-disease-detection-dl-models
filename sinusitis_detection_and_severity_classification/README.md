# X-Ray Waters View Classification API

This repository contains an API built using **FastAPI** to classify X-ray images as valid Waters View X-rays or invalid. The application is designed for quick deployment and easy accessibility using **Ngrok** for external testing.

---

## Features

- **Deep Learning-Powered**: Uses a pre-trained model to classify images.
- **FastAPI Framework**: High-performance API for seamless integration.
- **Ngrok Integration**: Exposes the API to be accessed from mobile or external devices.

---

## Requirements

- **Python 3.7+**
- **Required Libraries**:
  - `FastAPI`
  - `Uvicorn`
  - `TensorFlow`
- **Ngrok** (Download from [ngrok.com/download](https://ngrok.com/download)).

Install Python dependencies:
```bash
pip install fastapi uvicorn tensorflow
```
### Steps to Run the Application
#### Run the FastAPI Application.

To start the FastAPI server, use the following command:
```bash
uvicorn fast_api:app --reload --port 4000

# OR Use FastApi command

fastapi dev fast_api.py
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
